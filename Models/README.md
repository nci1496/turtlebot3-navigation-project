旧版README.md现已废弃
版本：
Ubuntu20.04
Ros Noetic
Gazebo 11.15.1
依赖:
可以先直接尝试启动launch文件，若出现缺少依赖的情况，再执行以下命令：
sudo apt update
sudo apt install ros-noetic-gazebo-ros ros-noetic-gazebo-ros-control ros-noetic-gazebo-plugins ros-noetic-teleop-twist-keyboard ros-noetic-robot-state-publisher ros-noetic-rviz -y
(以上命令中包含键盘控制的包)
安装完成以后，进入warehouse_world文件夹
在后打开终端，执行：
roslaunch warehouse_world.launch
此时环境应该正常加载出来了
新开终端，启动键盘控制：
rosrun teleop_twist_keyboard teleop_twist_keyboard.py


注意修改warehouse_world.launch里面的路径

