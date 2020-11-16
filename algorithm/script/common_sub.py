#!/usr/bin/env python
import rospy
from common_msgs.msg import common_msg
from common_msgs.srv import Notify_multiple_of_10, Notify_multiple_of_10Response

def callback(msg):
    print("subscrib x : {}, y : {}, z : {}".format(msg.point.x, msg.point.y, msg.point.z))

def service_callback(request):
    response = Notify_multiple_of_10Response(ten = "Multiplier of ten")
    print "request data : ", request.a, request.b, request.c, ", response : ", response.ten
    return response

rospy.init_node('common_subscriber')
sub = rospy.Subscriber('common_msg', common_msg, callback)
service = rospy.Service('Notify_10', Notify_multiple_of_10, service_callback)

rospy.spin()

