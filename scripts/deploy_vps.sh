#!/bin/bash
set -e

# Генеруємо унікальну назву
SERVER_NAME="gh-runner-$(date +%s)"

echo "=== 1. Отримання токена реєстрації ==="
RUNNER_TOKEN=$(curl -s -X POST -H "Authorization: token $GH_PAT" \
  "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/runners/registration-token" | jq -r '.token')

echo "=== 2. Генерація Cloud-Init скрипта ==="
cat << EOF > scripts/user_data.sh
#!/bin/bash
# Записуємо всі виводи в лог
exec > /var/log/user-data.log 2>&1
set -x

# Команда для видалення самого себе (Hetzner API)
cleanup() {
    SERVER_ID=\$(curl -s http://169.254.169.254/v1/meta-data/instance-id)
    curl -X DELETE -H "Authorization: Bearer $HCLOUD_TOKEN" "https://api.hetzner.cloud/v1/servers/\$SERVER_ID"
}

# Встановлення необхідного софту
apt-get update && apt-get install -y docker.io git curl jq python3-pip

# Налаштування раннера
useradd -m runner
mkdir -p /home/runner/actions-runner
cd /home/runner/actions-runner
curl -L -O https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz
chown -R runner:runner /home/runner

# Реєстрація та запуск
su - runner -c "cd /home/runner/actions-runner && ./config.sh --url https://github.com/$REPO_OWNER/$REPO_NAME --token $RUNNER_TOKEN --name $SERVER_NAME --labels self-hosted --ephemeral --unattended"
su - runner -c "cd /home/runner/actions-runner && ./run.sh"

# Видалення після завершення
cleanup
EOF

echo "=== 3. Створення сервера ==="
hcloud server create \
  --name "$SERVER_NAME" \
  --image "ubuntu-22.04" \
  --type "cx23" \
  --user-data-from-file scripts/user_data.sh