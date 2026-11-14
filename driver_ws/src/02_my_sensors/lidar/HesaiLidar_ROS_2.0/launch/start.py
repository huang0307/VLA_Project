from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 1. 获取包路径 (注意核对包名)
    pkg_dir = get_package_share_directory('hesai_ros_driver') 
    
    # 2. 定位配置文件
    yaml_config = pkg_dir + '/config/config.yaml'

    return LaunchDescription([
        Node(
            namespace='hesai_ros_driver', 
            package='hesai_ros_driver', 
            executable='hesai_ros_driver_node', 
            output='screen',
            # 🔥 加载你配置好的 yaml 文件
            parameters=[{'config_path': yaml_config}] 
        )
        # 👇 下面 rviz 的 Node 注释掉，不再跟着启动
        # ,Node(
        #     namespace='rviz2', 
        #     package='rviz2', 
        #     executable='rviz2', 
        #     arguments=['-d', pkg_dir + '/rviz/rviz2.rviz']
        # )
    ])