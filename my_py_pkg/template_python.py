#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class CustomNode(Node):

    def __init__(self): 
        super().__init__("custom_node")
        self.get_logger().info("Node has been started")
        self.counter = 0 
    
def main(args = None):
    rclpy.init(args=args) #init communication
    node = CustomNode()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()