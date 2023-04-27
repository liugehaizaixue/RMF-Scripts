import rclpy
from rclpy.node import Node
from rmf_fleet_msgs.msg import RobotState,Location,RobotMode #发

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('robot_state_publisher')
    publisher = node.create_publisher(RobotState, 'robot_state', 10)


    _robot_name = 'tinyRobot_1'
    _model = 'MyRobotModel'
    _task_id = '123'
    _seq = 1

    _mode = RobotMode()
    _mode.mode = 6

    _battery_percent = 75.0

    _location = Location()
    _location.t = node.get_clock().now().to_msg()
    _location.x = 29.33553715138718
    _location.y = -11.53732285932702
    _location.yaw = 1.5
    _location.level_name = "L1"
    _location.obey_approach_speed_limit = False
    _location.approach_speed_limit = 0.0

    message = RobotState(
      name = _robot_name,
      model = _model,
      battery_percent = _battery_percent,
      location = _location,
      task_id = _task_id,
      path = [],
      mode = _mode,
      seq = _seq,
    )


    publisher.publish(message)
    node.get_logger().info('Published robot state')

    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
