#!/bin/bash
set -e

SERVER_NAME="gh-runner-$(date +%s)"
FIREWALL_NAME="secure-runner-fw"

echo "=== 1. Setting up Firewall rules ==="
# Create firewall with zero inbound rules (All inbound SSH is completely blocked)
if ! hcloud firewall describe "$FIREWALL_NAME" >/dev/null 2>&1; then
  hcloud firewall create --name "$FIREWALL_NAME"
fi

echo "=== 2. Requesting GitHub Runner Registration Token ==="
RUNNER_TOKEN=$(curl -X POST -H "Authorization: token $GH_PAT" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/runners/registration-token" \
  | jq -r '.token')

if [ "$RUNNER_TOKEN" == "null" ] || [ -z "$RUNNER_TOKEN" ]; then
  echo "Error: Failed to obtain registration token from GitHub API."
  exit 1
fi

echo "=== 3. Generating dynamic Cloud-Init User Data ==="
cat << EOF > scripts/user_data.sh
#!/bin/bash
# Log all output of our initialization process to enable debugging via system logs
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
set -x

echo "=== Waiting for background system updates to finish ==="
while fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do
  echo "DPKG locked by another process, waiting 5 seconds..."
  sleep 5
done

echo "=== Installing system dependencies ==="
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y curl jq docker.io git python3-pip python3-venv build-essential libssl-dev libffi-dev nodejs

# Create runner user and add to docker group
useradd -m -s /bin/bash runner || true
usermod -aG docker runner || true

echo "=== Configuring GitHub Actions Runner package ==="
mkdir -p /home/runner/actions-runner && cd /home/runner/actions-runner

# Download the official stable version of the runner
curl -o actions-runner-linux-x64-2.316.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz

# Install system dependencies of the runner itself (required step by GitHub)
./bin/installdependencies.sh

# Change directory ownership to the newly created runner user
chown -R runner:runner /home/runner

echo "=== Registering the runner ==="
# Register runner under runner user (GitHub Actions prohibits running config as root)
su - runner -c "cd /home/runner/actions-runner && ./config.sh --url https://github.com/$REPO_OWNER/$REPO_NAME --token $RUNNER_TOKEN --name $SERVER_NAME --labels self-hosted --ephemeral --unattended"

echo "=== Starting task listener ==="
# Start the runner. This process will block and wait for jobs from our workflow
su - runner -c "cd /home/runner/actions-runner && ./run.sh"

echo "=== Tests completed. Triggering self-destruction of the VPS instance ==="
SERVER_ID=\$(curl -s http://169.254.169.254/v1/meta-data/instance-id)
curl -X DELETE -H "Authorization: Bearer $HCLOUD_TOKEN" "https://api.hetzner.cloud/v1/servers/\$SERVER_ID"
EOF

echo "=== 4. Launching VPS instance in Hetzner Cloud ==="
hcloud server create \
  --name "$SERVER_NAME" \
  --image "ubuntu-22.04" \
  --type "cx23" \
  --firewall "$FIREWALL_NAME" \
  --user-data-from-file scripts/user_data.sh