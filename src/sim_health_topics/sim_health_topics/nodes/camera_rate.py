import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from rclpy.qos import QoSProfile
from rclpy.duration import Duration

class CameraSim(Node):
    def __init__(self):
        super().__init__('sim_camera')
        qos = QoSProfile(depth=50, deadline=Duration(seconds=0.033))  # 30 Hz
        self.pub = self.create_publisher(Header, '/sim/camera_rate', qos)
        self.timer = self.create_timer(1.0 / 30.0, self.publish)

    def publish(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = "camera"
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(CameraSim())
    rclpy.shutdown()

if __name__ == "__main__":
    main()