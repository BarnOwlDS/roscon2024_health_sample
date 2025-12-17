import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Spam(Node):
    def __init__(self):
        super().__init__('sim_spam')
        self.pub = self.create_publisher(String, '/sim/diagnostic_spam', 10)
        self.timer = self.create_timer(0.01, self.publish)

    def publish(self):
        msg = String()
        msg.data = "spam"
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(Spam())
    rclpy.shutdown()

if __name__ == "__main__":
    main()