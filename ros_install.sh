#!/bin/bash
# ROS 2 Foxy (Ubuntu Focal) Installer
# See: https://index.ros.org/doc/ros2/Installation/Foxy/Linux-Install-Debians/

echo '[*] Installing ROS 2 Foxy (Ubuntu Focal).'

# Setup sources
echo '[*] Setting-up sources'
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Install ROS 2 packages
echo '[*] Installing ROS 2 packages'
sudo apt update
sudo apt install ros-foxy-desktop
sudo apt install ros-foxy-ros-base

# Sourcing setup script
echo '[*] Sourcing setup script'
source /opt/ros/foxy/setup.bash

# Install argcomplete (optional)
echo '[*] Installing argcomplete'
sudo apt install -y python3-pip
pip3 install -U argcomplete

# Install Tools
sudo apt install python3-colcon-common-extensions

echo '[*] All done.'