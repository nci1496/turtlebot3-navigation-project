#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SetModelState
from geometry_msgs.msg import Pose, Point, Quaternion

def main():
    rospy.init_node('moving_obstacles')

    model_name = rospy.get_param('~model_name', 'moving_box_obstacle')
    y_min      = rospy.get_param('~y_min',      -0.75)
    y_max      = rospy.get_param('~y_max',       0.75)
    speed      = rospy.get_param('~speed',       0.04)   # m/s
    rate_hz    = rospy.get_param('~rate',        20)

    x = 0.5
    y = 1.1
    z = 0.25
    direction = 1

    rospy.loginfo('[moving_obstacles] model=%s  y=[%.2f, %.2f]  speed=%.2f m/s',
                  model_name, y_min, y_max, speed)
    rospy.wait_for_service('/gazebo/set_model_state')
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

    rate = rospy.Rate(rate_hz)
    while not rospy.is_shutdown():
        y += direction * speed / rate_hz

        if y >= y_max:
            y = y_max
            direction = -1
        elif y <= y_min:
            y = y_min
            direction = 1

        target_pose = Pose(
            position=Point(x=x, y=y, z=z),
            orientation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        )

        from gazebo_msgs.msg import ModelState
        msg = ModelState()
        msg.model_name = model_name
        msg.pose = target_pose
        msg.reference_frame = 'world'

        try:
            set_state(msg)
        except rospy.ServiceException as e:
            rospy.logwarn_throttle(2.0, 'set_model_state call failed: %s', e)

        rate.sleep()

if __name__ == '__main__':
    main()
