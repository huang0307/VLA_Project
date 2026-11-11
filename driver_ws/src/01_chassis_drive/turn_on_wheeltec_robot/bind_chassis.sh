#!/bin/bash
# 只绑定底盘控制器为 /dev/wheeltec_controller

echo "正在为底盘绑定固定串口..."
# CP2102 芯片（常见于老款轮趣底盘）
echo 'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60",ATTRS{serial}=="0002", MODE:="0777", GROUP:="dialout", SYMLINK+="wheeltec_controller"' | sudo tee /etc/udev/rules.d/99-wheeltec-chassis.rules > /dev/null

# CH9102 芯片（常见于新款轮趣底盘）
echo 'KERNEL=="ttyCH343USB*", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d4",ATTRS{serial}=="0002", MODE:="0777", GROUP:="dialout", SYMLINK+="wheeltec_controller"' | sudo tee -a /etc/udev/rules.d/99-wheeltec-chassis.rules > /dev/null
echo 'KERNEL=="ttyACM*", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d4",ATTRS{serial}=="0002", MODE:="0777", GROUP:="dialout", SYMLINK+="wheeltec_controller"' | sudo tee -a /etc/udev/rules.d/99-wheeltec-chassis.rules > /dev/null

# 重新加载规则
sudo udevadm control --reload-rules
sudo udevadm trigger
echo "底盘绑定完成！请拔插底盘 USB 线生效。"