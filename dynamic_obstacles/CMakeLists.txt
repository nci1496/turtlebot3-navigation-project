cmake_minimum_required(VERSION 2.8.3)
project(dynamic_obstacles)

find_package(catkin REQUIRED COMPONENTS rospy gazebo_msgs geometry_msgs)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/moving_obstacles.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
