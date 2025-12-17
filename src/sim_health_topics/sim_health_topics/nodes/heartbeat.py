import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from rclpy.qos import QoSProfile
from rclpy.duration import Duration

class HeartbeatNode(Node):
    def __init__(self):
        super().__init__('sim_heartbeat')
        qos = QoSProfile(depth=1, deadline=Duration(seconds=1.0))
        self.pub = self.create_publisher(Bool, '/sim/heartbeat', qos)
        self.timer = self.create_timer(0.5, self.tick)

    def tick(self):
        msg = Bool()
        msg.data = True
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(HeartbeatNode())
    rclpy.shutdown()

if __name__ == "__main__":
    main()