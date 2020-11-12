#!/usr/bin/env python
import rospy
from common_msgs.msg import common_msg

def callback(msg):
    print("subscrib x : {}, y : {}, z : {}".format(msg.point.x, msg.point.y, msg.point.z))
rospy.init_node('common_subscriber')
sub = rospy.Subscriber('common_msg', common_msg, callback)
rospy.spin()

