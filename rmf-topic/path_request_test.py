import rclpy
from rclpy.node import Node
from rmf_fleet_msgs.msg import RobotState, Location, PathRequest


class PathRequestNode(Node):

    def __init__(self):
        super().__init__('path_request_node')
        self.path_pub = self.create_publisher(PathRequest, 'robot_path_requests', 10)
        self.publish_path()

    def publish_path(self):
        task_id = 'test_task_id'
        fleet_name = "tinyRobot"
        robot_name = "tinyRobot1"
        path_request = PathRequest()
        target_loc = Location()
        target_loc.t = self.get_clock().now().to_msg()
        target_loc.x = 29.33553715138718
        target_loc.y = -11.53732285932702
        target_loc.yaw = 1.5
        target_loc.level_name = "L2"
        target_loc.obey_approach_speed_limit = False
        target_loc.approach_speed_limit = 0.0

        target_loc2 = Location()
        target_loc2.t = self.get_clock().now().to_msg()
        target_loc2.x = 29.33553715138718
        target_loc2.y = -11.53732285932702
        target_loc2.yaw = 1.5
        target_loc2.level_name = "L2"
        target_loc2.obey_approach_speed_limit = False
        target_loc2.approach_speed_limit = 0.0
        path_request.path.append(target_loc)
        path_request.path.append(target_loc2)
        path_request.fleet_name = fleet_name
        path_request.robot_name = robot_name
        path_request.task_id = task_id
        # 设置 Path 消息对象的内容
        # ...
        self.path_pub.publish(path_request)
        self.get_logger().info('Published Path message.')

def main(args=None):
    rclpy.init(args=args)
    node = PathRequestNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
