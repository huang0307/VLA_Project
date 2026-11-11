==================================================
WHEELTEC R550 PLUS (AKM) 底盘配置与启动说明
配置日期：2026-11-11
==================================================

【基本参数】
车型参数：senior_akm
底盘高度补偿(base_link Z轴)：0.03826
通讯串口别名：/dev/wheeltec_controller

--------------------------------------------------
一、环境准备与前置依赖 (WSL2端)
--------------------------------------------------
1. 安装必要的 ROS 2 依赖包：
   sudo apt update
   sudo apt install ros-humble-imu-filter-madgwick
   sudo apt install ros-humble-robot-localization

2. WSL2 USB 穿透 (在 Windows PowerShell 中执行)：
   usbipd list
   usbipd attach --wsl --busid <你的BUSID> --auto-attach

--------------------------------------------------
二、串口别名绑定
--------------------------------------------------
1. 进入目录并赋予权限：
   cd ~/VLA_Project/driver_ws/src/01_chassis_drive/turn_on_wheeltec_robot
   chmod +x bind_chassis.sh

2. 运行脚本：
   sudo ./bind_chassis.sh

3. 拔插 USB 线后，验证别名：
   ls /dev | grep wheeltec
   (看到 wheeltec_controller 即为成功)

--------------------------------------------------
三、Launch 文件必要修改
--------------------------------------------------
1. turn_on_wheeltec_robot.launch.py (总管家)
   - 修改 base_to_link 的 Z 轴参数为 '0.03826'
   - 启用旗舰款车型：flagship_type，参数填 'senior_akm': 'true'
   - 注释掉：minibot_type

2. robot_mode_description.launch.py (模型描述)
   - 仅保留 senior_akm 代码块
   - 当前过渡阶段：注释掉 3D模型加载(URDF)、相机TF、雷达TF

--------------------------------------------------
四、日常启动与测试
--------------------------------------------------
1. 启动底盘总控 (终端 1)：
   cd ~/VLA_Project/driver_ws
   colcon build --packages-select turn_on_wheeltec_robot
   source install/setup.bash
   ros2 launch turn_on_wheeltec_robot turn_on_wheeltec_robot.launch.py
   
   *成功标志：终端输出 wheeltec_robot serial port opened

2. 发送控制指令 (终端 2)：
   cd ~/VLA_Project/driver_ws
   source install/setup.bash
   ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
   *按 Ctrl+C 停止，底盘会自动刹车。

3. 数据验证 (终端 3)：
   cd ~/VLA_Project/driver_ws
   source install/setup.bash
   
   * 验证融合里程计 (推车看 x 坐标变化)：
   ros2 topic echo /odom_combined
   
   * 验证 IMU 角速度 (原地转圈看数值变化)：
   ros2 topic echo /imu/data --field angular_velocity.z
   
   * 查看 TF 树连通性：
   ros2 run tf2_ros tf2_echo odom_combined base_footprint

==================================================