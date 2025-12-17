import rclpy, random
from rclpy.node import Node
from sensor_msgs.msg import Temperature
from rclpy.qos import QoSProfile
from rclpy.duration import Duration

class TempSensor(Node):
    def __init__(self):
        super().__init__('sim_temp_sensor')
        qos = QoSProfile(depth=10, deadline=Duration(seconds=0.2))
        self.pub = self.create_publisher(Temperature, '/sim/sensor_temp', qos)
        self.timer = self.create_timer(0.1, self.publish)

    def publish(self):
        msg = Temperature()
        msg.temperature = 20.0 + random.uniform(-2, 2)
        msg.variance = 0.5
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(TempSensor())
    rclpy.shutdown()

if __name__ == "__main__":
    main()
