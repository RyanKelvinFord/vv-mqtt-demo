#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update -y && sudo apt upgrade -y

# Install necessary packages for Docker
echo "Installing packages for Docker..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
echo "Adding Docker's official GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker's official APT repository
echo "Adding Docker's official APT repository..."
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update the package database with Docker packages
echo "Updating the package database with Docker packages..."
sudo apt update -y

# Install Docker
echo "Installing Docker..."
sudo apt install -y docker-ce

# Add the current user to the Docker group
echo "Adding the current user to the Docker group..."
sudo usermod -aG docker ${USER}

# Install Git
echo "Installing Git..."
sudo apt install -y git

# Print Docker and Git versions
echo "Docker and Git installation completed."
docker --version
git --version

echo "Installation script completed. Please log out and log back in to apply Docker group changes."
