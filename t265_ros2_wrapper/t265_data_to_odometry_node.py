import rclpy
from rclpy.node import Node

from ros2_custom_msgs.msg import T265
from nav_msgs.msg import Odometry

class T265OdometryPublisher(Node):

    def __init__(self):
        super().__init__('t265_odometry_publisher')
        self.publisher_ = self.create_publisher(Odometry, 't265/odom', 10)
        self.subscriber = self.create_subscription( T265,'t265', self.t265_callback, 10)
        self.subscriber

    def t265_callback(self, t265msg):
        msg = Odometry
        msg.pose.pose.position.x = t265msg.position.x
        msg.pose.pose.position.y = t265msg.position.y
        msg.pose.pose.position.z = t265msg.position.z
        msg.pose.pose.orientation.x = t265msg.orientation.x
        msg.pose.pose.orientation.y = t265msg.orientation.y
        msg.pose.pose.orientation.z = t265msg.orientation.z
        

        msg.twist.linear.x = t265msg.velocity.x
        msg.twist.linear.y = t265msg.velocity.y
        msg.twist.linear.z = t265msg.velocity.z
        msg.twist.angular.x = t265msg.angular_velocity.x
        msg.twist.angular.y = t265msg.angular_velocity.y
        msg.twist.angular.z = t265msg.angular_velocity.z

        msg.child_frame_id = "t265_camera"
        msg.header.stamp = self.get_clock().now().to_msg()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    t265_publisher =T265OdometryPublisher()

    rclpy.spin(t265_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t265_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()