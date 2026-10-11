import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String
from driverless_msgs.srv import PalindromeCheck

class Node2(Node):
    def __init__(self):
        super().__init__('node2')
        self.sub = self.create_subscription(RT2String, '/string_topic', self.string_callback, 10)
        self.cli = self.create_client(PalindromeCheck, 'check_palindrome_service')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Node 3 service to start...')

    def string_callback(self, msg):
        s = msg.data
        # 1 if true (palindrome), 0 if false
        is_palindrome = 1 if s == s[::-1] else 0 
        
        req = PalindromeCheck.Request()
        req.is_palindrome = is_palindrome
        self.future = self.cli.call_async(req)
        self.future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Node 3 output: {response.response}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()