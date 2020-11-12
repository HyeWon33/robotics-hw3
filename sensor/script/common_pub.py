#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import common_msg

rospy.init_node('common_publisher')
pub = rospy.Publisher('common_msg', common_msg, queue_size=10)
msg = common_msg()
rate = rospy.Rate(10)
count = 0.0
while not rospy.is_shutdown():
    count += 1.0
    msg.data = count
    msg.point = Point(x = count, y = count, z = count)
    pub.publish(msg)
    print("publish x : {}, y : {}, z : {}".format(msg.point.x, msg.point.y, msg.point.z))
    rate.sleep()

