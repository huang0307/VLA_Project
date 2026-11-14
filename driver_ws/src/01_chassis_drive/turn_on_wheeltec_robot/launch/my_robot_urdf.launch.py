import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 1. 指定你要加载的主 URDF 文件名
    # 文件在 wheeltec_robot_urdf 包的 urdf 目录下
    urdf_file_name = 'senior_akm_robot.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('wheeltec_robot_urdf'),
        'urdf',
        urdf_file_name
    )

    # 2. 读取 URDF 文件内容
    try:
        with open(urdf_path, 'r') as infp:
            robot_desc = infp.read()
    except FileNotFoundError:
        raise Exception(f"找不到 URDF 文件: {urdf_path}")

    # 3. 启动 robot_state_publisher 节点
    # 解析 URDF，并自动发布里面定义的所有固定/活动关节的 TF 变换
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    return LaunchDescription([
        rsp_node
    ])