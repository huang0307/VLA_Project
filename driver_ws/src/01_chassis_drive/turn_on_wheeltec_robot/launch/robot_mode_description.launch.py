import os
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_robot_node(robot_urdf, child):
    return launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name=f'robot_state_publisher_{child}',
        arguments=[os.path.join(get_package_share_directory('wheeltec_robot_urdf'), 'urdf', robot_urdf)],
    )

def generate_static_transform_publisher_node(translation, rotation, parent, child):
    return launch_ros.actions.Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name=f'base_to_{child}',
        arguments=[translation[0], translation[1], translation[2], rotation[0], rotation[1], rotation[2], parent, child],
    )

def generate_launch_description():
    senior_akm = LaunchConfiguration('senior_akm', default='true')

    senior_akm_ = GroupAction(
        condition=IfCondition(senior_akm),
        actions=[
            # 1. URDF 模型（已注释，暂不加载）
            # generate_robot_node('senior_akm_robot.urdf','senior_akm'),
            
            # 2. 雷达 TF 坐标（已注释，暂不发布）
            # generate_static_transform_publisher_node(['0.08874', '0.00067', '0.11102'], ['0', '0', '0'], 'base_footprint', 'laser'),
            
            # 3. 相机 TF 坐标（已注释，暂不发布）
            # generate_static_transform_publisher_node(['0.16578', '0.00095', '0.0897'], ['0', '0', '0'], 'base_footprint', 'camera_link'),      
        ]) 

    ld = LaunchDescription()
    ld.add_action(senior_akm_)
    return ld