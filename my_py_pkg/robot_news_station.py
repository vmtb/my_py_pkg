#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):

    def __init__(self): 
        super().__init__("robot_news_station")

        self.robot_name = "C3P0"
        self.publisher_ = self.create_publisher(String, 'robot_news', 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started")


    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is "+str(self.robot_name)+" from the robot news station."        
        self.publisher_.publish(msg)
    

def main(args = None):
    rclpy.init(args=args) #init communication
    node = RobotNewsStationNode()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()