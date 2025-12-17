import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from rclpy.duration import Duration

class CmdVel(Node):
    def __init__(self):
        super().__init__('sim_cmd_vel')
        qos = QoSProfile(depth=10, deadline=Duration(seconds=0.1))
        self.pub = self.create_publisher(Twist, '/sim/cmd_velocity', qos)
        self.timer = self.create_timer(0.05, self.publish)

    def publish(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.1
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(CmdVel())
    rclpy.shutdown()

if __name__ == "__main__":
    main()
