#/bin/bash
# Configure project environnment variables for ROS, Python, etc.

set -e
set -a
PROJECT_WORKSPACE=~/devel/tortello

echo "[*] Setting-up ROS Foxy (sourcing and exports)"
source /opt/ros/foxy/setup.sh
source $PROJECT_WORKSPACE/install/setup.bash
GAZEBO_MODEL_PATH=$PROJECT_WORKSPACE/src/turtlebot3_simulations/turtlebot3_gazebo/models
TURTLEBOT3_MODEL=burger

echo "[*] Activating Python environment $PYTHON_VENV"
PYTHON_VENV=$PROJECT_WORKSPACE/env/tortello_desktop/bin/activate
source $PYTHON_VENV

# Disable flags
set +e
set +a
echo "[*] Done."        
