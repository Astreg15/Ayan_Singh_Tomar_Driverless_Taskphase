import rclpy
from rclpy.node import Node
from driverless_msgs.srv import PalindromeCheck

class Node3(Node):
    def __init__(self):
        super().__init__('node3')
        self.srv = self.create_service(PalindromeCheck, 'check_palindrome_service', self.check_callback)

    def check_callback(self, request, response):
        if request.is_palindrome == 1:
            response.response = "Yes"
        else:
            response.response = "No"
            
        self.get_logger().info(f'Received indicator {request.is_palindrome}. Conveying: {response.response}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()