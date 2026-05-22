#!/bin/bash
set -e

# Унікальна назва сервера
SERVER_NAME="gh-runner-$(date +%s)"

echo "=== 1. Отримання токена реєстрації ==="
RUNNER_TOKEN=$(curl -s -X POST -H "Authorization: token $GH_PAT" \
  "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/runners/registration-token" | jq -r '.token')

echo "=== 2. Створення сервера через Hetzner API ==="
hcloud server create \
  --name "$SERVER_NAME" \
  --image "ubuntu-22.04" \
  --type "cx23" \
  --user-data "#!/bin/bash
# Логування всіх дій для дебагу
exec > /var/log/user-data.log 2>&1
set -x

# 1. Встановлення залежностей, необхідних для роботи GitHub Runner (.NET runtime dependencies)
apt-get update && apt-get install -y \
  docker.io git curl jq python3-pip \
  libicu-dev libssl-dev libkrb5-3 zlib1g

# 2. Підготовка користувача
useradd -m runner
mkdir -p /home/runner/actions-runner
cd /home/runner/actions-runner

# 3. Завантаження та розпакування раннера
curl -L -O https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz
chown -R runner:runner /home/runner

# 4. Конфігурація та запуск від імені користувача 'runner'
su - runner -c 'cd /home/runner/actions-runner && ./config.sh --url https://github.com/$REPO_OWNER/$REPO_NAME --token $RUNNER_TOKEN --name $SERVER_NAME --labels self-hosted --ephemeral --unattended'
su - runner -c 'cd /home/runner/actions-runner && ./run.sh'
"
echo "Сервер $SERVER_NAME успішно запущено."