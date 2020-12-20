
# Following: https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/

# INSTALL & BUILD
# cd src
# git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
# cd ..
# colcon build

source ./install/setup.sh
source /opt/ros/foxy/setup.sh 


export GAZEBO_MODEL_PATH=$(pwd)/src/turtlebot3_simulations/turtlebot3_gazebo/models/
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py

# Next step: 
# Collision avoidance, Visualize Simulation Data (Rviz), SLAM
# https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/