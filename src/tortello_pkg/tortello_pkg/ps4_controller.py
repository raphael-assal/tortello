#!/usr/bin/env python
from pyPS4Controller.controller import Controller

# Typically, the Input Handler (or an AI) produces commands.
# The dispatcher or actor itself then consumes command and invokes them.
# In between, we could even place a queue.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPublisher(Node):
    def __init__(self):
        super().__init__('vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    def publish(self, msg: Twist):
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

class PublisherAdapter:
    """
        Adapts controller calls to ROS Publisher 
        while providing basic input filtering and normalization.
    """
    def __init__(self, publisher):
        self.publisher_ = publisher
        
    def __call__(self, value):
        msg = self.make_msg(self.normalize(value))
        self.publisher_.publish(msg)

    def make_msg(self, value):
        return value

    def normalize(self, value):
        return value / 1

class VerticalAccelerationAdapter(PublisherAdapter):
    def make_msg(self, value):
        msg = Twist()
        msg.linear.x = self.normalize(value)
        return msg

class HorizontalAccelerationAdapter(PublisherAdapter):
    def make_msg(self, value):
        msg = Twist()
        msg.linear.y = self.normalize(value)
        return msg

class BlankController(Controller):
    def __init__(self, interface, connecting_using_ds4drv):
        super().__init__(interface, connecting_using_ds4drv=connecting_using_ds4drv)
        event_listeners = [att for att in dir(self) if 'on_' in att and callable(getattr(self, att))]
        for m in event_listeners:
            setattr(self, m, lambda *args: None)

# Controller & Command Mapping
rclpy.init()
vel_publisher = VelPublisher()
robot_controller = BlankController(interface="/dev/input/js0", connecting_using_ds4drv=False)
robot_controller.on_L3_up = VerticalAccelerationAdapter(vel_publisher)
robot_controller.on_L3_down = VerticalAccelerationAdapter(vel_publisher)
#robot_controller.on_L3_right = HorizontalAccelerationAdapter(vel_publisher)
#robot_controller.on_L3_left = HorizontalAccelerationAdapter(vel_publisher)
robot_controller.listen()
