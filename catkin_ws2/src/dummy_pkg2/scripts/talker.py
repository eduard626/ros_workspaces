#!/usr/bin/python3

import rospy
from std_msgs.msg import String
import rospkg
import os

if __name__=="__main__":
    rospy.init_node("talker")
    rate = rospy.Rate(10)
    pub = rospy.Publisher("topic", String, queue_size=1)
    # get the current ws
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path("dummy_pkg2")
    cmake_prefix = os.environ["CMAKE_PREFIX_PATH"]
    while not rospy.is_shutdown():
        rate.sleep()
        pub.publish(f"Package path {pkg_path}\nPrefix {cmake_prefix}")
