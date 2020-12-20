#/bin/bash

set -e
source /opt/ros/foxy/setup.sh
source ./install/setup.bash
export ROS_DOMAIN_ID=30 #TURTLEBOT3

export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(pwd)/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models
