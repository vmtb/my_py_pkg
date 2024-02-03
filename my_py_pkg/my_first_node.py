#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self): 
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello ROS 2 OOP")
        self.create_timer(0.5, self.timer_callback) #2Hz = 1/2 = 0.5s

    def timer_callback(self):
        self.counter+=1
        self.get_logger().info("Hello !!"+str(self.counter))

def main(args = None):
    rclpy.init(args=args) #init communication
    node = MyNode()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()