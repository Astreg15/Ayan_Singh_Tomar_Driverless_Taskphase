import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.pub = self.create_publisher(RT2String, '/string_topic', 10)
        self.user_string = input("Enter a string (e.g. AABAA): ")
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = RT2String()
        msg.data = self.user_string
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()