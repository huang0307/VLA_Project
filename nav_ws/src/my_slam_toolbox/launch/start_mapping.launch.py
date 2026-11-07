import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 找到参数文件路径
    config_dir = os.path.join(get_package_share_directory('my_slam_toolbox'), 'config')
    param_file = os.path.join(config_dir, 'mapper_params.yaml')

    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[param_file]
        )
    ])