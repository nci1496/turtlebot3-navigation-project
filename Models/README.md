# Models 使用说明

本目录下的仓储场景用于移动机器人仿真实验，运行环境如下：

- Ubuntu 20.04
- ROS Noetic
- Gazebo 11.15.1

## 依赖安装

可以先直接尝试启动对应命令；若运行过程中提示缺少依赖，再执行以下安装命令：

```bash
sudo apt update
sudo apt install ros-noetic-gazebo-ros ros-noetic-gazebo-ros-control ros-noetic-gazebo-plugins ros-noetic-teleop-twist-keyboard ros-noetic-robot-state-publisher ros-noetic-rviz ros-noetic-map-server ros-noetic-turtlebot3-slam ros-noetic-turtlebot3-navigation -y
```

## 建图阶段命令

### 终端1：启动世界

```bash
roslaunch /home/nci/sim_ws/src/Models/warehouse_world/warehouse_world.launch
```

### 终端2：启动 SLAM 建图

```bash
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### 终端3：运行 `robot_state_publisher`

```bash
rosrun robot_state_publisher robot_state_publisher
```

### 终端4：开启移动节点

```bash
rosrun walk pub
```

### 终端5：开启键盘控制

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

机器人遍历环境完成建图后，执行地图保存命令。

### 终端6：保存地图

```bash
rosrun map_server map_saver -f warehouse_world_small
```

保存完成后，关闭 RViz，以及建图阶段使用的终端2、3、4、5、6。

## 导航阶段命令

### 终端7：启动动态障碍物

```bash
MOVING_OBSTACLE_SPEED=0.04 roslaunch dynamic_obstacles spawn_boxes.launch
```

### 终端8：打开地图导航

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/maps/warehouse_world_small.yaml
```

### 终端3：再次运行 `robot_state_publisher`

```bash
rosrun robot_state_publisher robot_state_publisher
```

## RViz 操作

1. 使用 `2D Pose Estimate` 初始化机器人位置。
2. 使用 `2D Nav Goal` 设置目标点并开始导航。

## 说明

- 若你的工作空间路径不是 `/home/nci/sim_ws`，请自行修改第一条 `roslaunch` 命令中的绝对路径。
- 注意，除了命令的路径要改以外，第一条命令里的warehouse_world.launch，里面的路径也要改
- 若地图保存路径与 `$HOME/maps/warehouse_world_small.yaml` 不一致，请同步修改导航命令中的 `map_file` 参数。
