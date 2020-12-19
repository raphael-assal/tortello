#!/bin/bash
# ROS 2 commands reference

echo "This isn't supposed to run. Duh."
exit 0

# Create package
ros2 pkg create --build-type ament_python <package>
ros2 pkg create <pkg-name> --dependencies [deps]

# Build package
colcon build --packages-select <my_package>

# Run package
ros2 run my_package my_node

# Check/Install dependencies (to run from root dir)
rosdep install -i --from-path src --rosdistro foxy -y