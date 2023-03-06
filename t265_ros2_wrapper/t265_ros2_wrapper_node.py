import rclpy
from rclpy.node import Node

from ros2_custom_msgs.msg import T265

import pyrealsense2 as rs

class T265DataPublisher(Node):

    def __init__(self):
        super().__init__('t265_data_publisher')
        self.publisher_ = self.create_publisher(T265, 't265', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.pipe = rs.pipeline()
        self.cfg = rs.config()
        self.cfg.enable_stream(rs.stream.pose)
        self.pipe.start(self.cfg)

    def timer_callback(self):
        frames = self.pipe.wait_for_frames()
        pose = frames.get_pose_frame()
        if pose:
            data = pose.get_pose_data()      
            msg =  T265()
            msg.position.position.x = data.translation.x
            msg.position.position.y = data.translation.y
            msg.position.position.z = data.translation.z
            msg.position.orientation.x = data.rotation.x
            msg.position.orientation.y = data.rotation.y
            msg.position.orientation.z = data.rotation.z
            msg.position.orientation.w = data.rotation.w

            msg.velocity.linear.x = data.velocity.x
            msg.velocity.linear.y = data.velocity.y
            msg.velocity.linear.z = data.velocity.z
            msg.velocity.angular.x = data.angular_velocity.x
            msg.velocity.angular.y = data.angular_velocity.y
            msg.velocity.angular.z = data.angular_velocity.z

            msg.acceleration.linear.x = data.acceleration.x
            msg.acceleration.linear.y = data.acceleration.y
            msg.acceleration.linear.z = data.acceleration.z
            msg.acceleration.angular.x = data.angular_acceleration.x
            msg.acceleration.angular.y = data.angular_acceleration.y
            msg.acceleration.angular.z = data.angular_acceleration.z

            msg.header.frame_id = "t265_camera"
            msg.header.stamp = self.get_clock().now().to_msg()

            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    t265_publisher =T265DataPublisher()

    rclpy.spin(t265_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t265_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()