#!/bin/bash

# setup_vps.sh
# Run this on your Cloud VPS (Ubuntu/Debian) to set up the bot.

echo ">>> Updating System..."
sudo apt-get update && sudo apt-get upgrade -y

echo ">>> Installing Docker & Git..."
sudo apt-get install -y docker.io docker-compose git

echo ">>> Starting Docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo ">>> Setting up Project..."
# Create directory
mkdir -p ~/freefire-bot
cd ~/freefire-bot

# NOTE: You need to clone your repo here. 
# Since I don't know your exact repo URL, I'll ask for it.
read -p "Enter your GitHub Repository URL (e.g., https://github.com/user/repo.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "No URL provided. Exiting."
    exit 1
fi

echo ">>> Cloning $REPO_URL..."
git clone "$REPO_URL" .

echo ">>> Building and Starting Cloud Bot..."
sudo docker-compose up -d --build

echo ">>> DONE! Your bot is running."
echo "Access Dashboard at: http://$(curl -s ifconfig.me):5000"
echo "Access Emulator at: http://$(curl -s ifconfig.me):6080"
