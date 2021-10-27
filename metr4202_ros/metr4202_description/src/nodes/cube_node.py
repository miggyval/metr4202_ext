#!/usr/bin/ python  

import rospy
import tf
from tf import broadcaster
from math import *

def publish_pose(x, y, z, phi):
    br = tf.TransformBroadcaster()
    br.sendTransform((x, y, z), (0, 0, sin(phi / 2), cos(phi / 2)), rospy.Time.now(), "cube_link", "world")

if __name__ == '__main__':
    rospy.init_node('cube_node')
    rate = rospy.Rate(2000)
    start_time = rospy.Time.now()
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        t = (current_time - start_time).to_sec()
        f = 0.1
        publish_pose(2 * cos(2 * pi * f * t), 2 * sin(2 * pi * f * t), 0.5, 2 * pi * f * t)
        rate.sleep()