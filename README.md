按照你现在已经验证成功的情况，这是你从零开始做到动态导航前的完整命令链。

---

# 1. 启动仿真环境

先设置机器人型号：
（好像默认就有，
grep TURTLEBOT3_MODEL ~/.bashrc 
输出export TURTLEBOT3_MODEL=burger就行）

```bash
export TURTLEBOT3_MODEL=burger
```

启动 Gazebo：

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

验证：

```bash
rostopic list
```

应该能看到：

```text
/scan
/odom
/cmd_vel
/tf
```

---

# 3. 建图（gmapping）

新终端：

启动 SLAM：

```bash
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

---

# 4. 启动键盘控制

新终端：

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

新终端：

```bash
rosrun walk pub
```

---

# 5. 保存地图

机器人走完整个场景后：

```bash
mkdir -p ~/maps
```

保存地图：

```bash
rosrun map_server map_saver -f ~/maps/stage1
```

得到：

```text
~/maps/stage1.pgm
~/maps/stage1.yaml
```

---

# 6. 关闭建图

关闭：

```text
gmapping
teleop
walk
rviz
```

保留 Gazebo。

---

# 7. 加载地图

新终端：

```bash
rosrun map_server map_server ~/maps/stage1.yaml
```

---

# 8. 启动导航系统

新终端：

```bash
export TURTLEBOT3_MODEL=burger
```

启动：

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch \
map_file:=$HOME/maps/stage1.yaml
```

这个会启动：

```text
map_server
AMCL
move_base
RViz
```

（实际上你自己单独启动 map_server 也能用，不过后面建议只保留这个 launch）

---

# 9. AMCL初始化

RViz中：

```text
2D Pose Estimate
```

点击机器人实际位置。

拖出机器人朝向。

等待几秒。

地图与激光重合。

---

# 10. 自动导航

RViz中：

```text
2D Nav Goal
```

点击目标位置。

拖出目标朝向。

机器人自动：

```text
全局规划
↓
局部规划
↓
路径跟踪
↓
到达目标
```

---

# 验证命令(不用执行)

## 查看AMCL

```bash
rostopic echo /amcl_pose
```

---

## 查看TF

```bash
rosrun tf tf_echo map odom
```

---

## 查看move_base

```bash
rosnode list | grep move
```

应该看到：

```text
/move_base
```

---

## 查看规划路径

```bash
rostopic list | grep plan
```

一般有：

```text
/move_base/NavfnROS/plan
/move_base/DWAPlannerROS/local_plan
```

---

# 当前TF树

你最终确认正常的是：

```text
map
 ↓
odom
 ↓
base_footprint
 ↓
base_link
 ├── base_scan
 ├── imu_link
 └── caster_back_link
```

完全正常。

---

# 课程要求对应关系


| 课程要求    | 你的实现                     |
| ------- | ------------------------ |
| 环境感知    | 激光雷达 + gmapping          |
| 栅格地图构建  | stage1.pgm + stage1.yaml |
| 移动机器人定位 | AMCL                     |
| 路径规划    | Global Planner(A*)       |
| 轨迹规划    | DWA                      |
| 路径跟踪    | move_base 输出 `/cmd_vel`  |
| 到达目标点   | 2D Nav Goal 成功           |


---

# 下一阶段（准备加分）

准备新增：

```text
dynamic_obstacles
├── launch
│   └── spawn_boxes.launch
└── scripts
    └── moving_obstacles.py
```

实现：

```text
动态障碍物
↓
DWA动态避障
↓
到达目标
```

这一步完成后，你的项目展示效果会比单纯 TurtleBot3 官方 Demo 强不少，而且不需要推翻现有系统。