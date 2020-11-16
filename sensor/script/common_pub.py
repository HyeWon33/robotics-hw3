#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import common_msg
from common_msgs.srv import Notify_multiple_of_10, Notify_multiple_of_10Request

rospy.init_node('common_publisher')
pub = rospy.Publisher('common_msg', common_msg, queue_size=10)
requester = rospy.ServiceProxy('Notify_10', Notify_multiple_of_10)
rospy.wait_for_service('Notify_10')
msg = common_msg()
rate = rospy.Rate(10)
count = 0.0

while not rospy.is_shutdown():
    if count % 10.0 == 0.0:
        req = Notify_multiple_of_10Request(a=count, b=count, c=count)
        res = requester(req)
        print "request data : ", req.a, req.b, req.c, ", response : ", res.ten
    count += 1.0
    msg.data = count
    msg.point = Point(x = count, y = count, z = count)
    pub.publish(msg)
    print("publish x : {}, y : {}, z : {}".format(msg.point.x, msg.point.y, msg.point.z))
    rate.sleep()

