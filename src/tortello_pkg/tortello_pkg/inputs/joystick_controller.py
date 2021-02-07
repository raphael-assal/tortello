import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from collections import defaultdict
import pygame

"""
    Adapted from: 
    https://github.com/ChristianD37/YoutubeTutorials/blob/master/PS4%20Controller/test.py
"""

class InputHandler:
    def __init__(self, callbacks={}):
        self.callbacks = defaultdict(lambda: lambda: None, callbacks)

    def handle_input(self, event):
        # HANDLING ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:

            # Horizontal Analog
            if event.axis == 0 and abs(event.value) > .4:
                if event.value < -.7:
                    return self.callbacks['on_joystick_left'](event.value)
                if event.value > .7:
                    return self.callbacks['on_joystick_right'](event.value)

            # Vertical Analog
            if event.axis == 1 and abs(event.value) > .4:
                if event.value < -.7:
                    return self.callbacks['on_joystick_up'](event.value)
                if event.value > .7:
                    return self.callbacks['on_joystick_down'](event.value)


class AccelerateXCommand:
    def __init__(self, value):
        self.value = float(value)

    def __call__(self, target, *args, **kwds):
        target.accelerate_x(self.value, *args, **kwds)

class AccelerateYCommand:
    def __init__(self, value):
        self.value = float(value)

    def __call__(self, target, *args, **kwds):
        target.accelerate_y(self.value, *args, **kwds)

class PlanarRobot(Node):
    def __init__(self, x=.0, y=.0, verbose=False):
        self.x = x
        self.y = y
        self.verbose = verbose

        super().__init__('planar_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    def __repr__(self):
        return f"PlanarRobot({self.x, self.y})"

    def accelerate_x(self, dx, dt=1.):
        self.x += dx * dt

    def accelerate_y(self, dy, dt=1.):
        self.y += dy * dt

    def publish_state(self):
        state = Twist()
        state.linear.x = self.x
        state.linear.y = self.y


        self.publisher_.publish(state)
        if self.verbose:
            msg = f'Publishing: {state}'
            self.get_logger().info(msg)
        


if __name__ == '__main__':
    # Initialization
    rclpy.init()

    pygame.init()
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print(f'Joystick({i}) initialized.')

    # Input handling
    callbacks = {
        'on_joystick_up': AccelerateXCommand,
        'on_joystick_down': AccelerateXCommand,
        'on_joystick_left': AccelerateYCommand,
        'on_joystick_right': AccelerateYCommand
    }
    input_handler = InputHandler(callbacks)
    planar_robot = PlanarRobot(verbose=True)
    
    while rclpy.ok():
        for event in pygame.event.get():
            input_command = input_handler.handle_input(event)
            if input_command:
                input_command(planar_robot)
            planar_robot.publish_state()