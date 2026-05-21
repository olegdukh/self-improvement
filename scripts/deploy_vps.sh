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
# Clean API URL without any markdown brackets
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
set -e

# Install required stack dependencies
export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get install -y curl jq docker.io git python3-pip

# Setup GitHub Actions Runner package
mkdir -p /home/runner && cd /home/runner
curl -o actions-runner-linux-x64-2.316.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz

useradd -m runner || true
chown -R runner:runner /home/runner

# Register runner with --ephemeral flag (will self-remove after executing exactly 1 job)
su - runner -c "./config.sh --url https://github.com/$REPO_OWNER/$REPO_NAME --token $RUNNER_TOKEN --name $SERVER_NAME --ephemeral --unattended"

# Start the listener loop. This blocks until GitHub assigns the job, executes it, and exits
su - runner -c "./run.sh"

echo "=== Tests completed. Triggering self-destruction of VPS instance ==="
SERVER_ID=\$(curl -s http://169.254.169.254/v1/meta-data/instance-id)
curl -X DELETE -H "Authorization: Bearer $HCLOUD_TOKEN" "https://api.hetzner.cloud/v1/servers/\$SERVER_ID"
EOF

echo "=== 4. Launching VPS Instance on Hetzner Cloud ==="
# Using universally available cx21 type to guarantee provisioning compatibility
hcloud server create \
  --name "$SERVER_NAME" \
  --image "ubuntu-22.04" \
  --type "cx21" \
  --firewall "$FIREWALL_NAME" \
  --user-data-from-file scripts/user_data.sh