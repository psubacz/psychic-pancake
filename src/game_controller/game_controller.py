#!/usr/bin/env python

import rospy
from std_msgs.msg import String
'''
game controller node

setups a bluetooth game controller node.

basic flow:
    init the controller
    while not dead:
        if no controller found
            pub false
            continue
        else:
            pub true
            handle gamepad logic
            pub incoming [controller_id, button_prompts, etc...]
'''

def talker():
    pub = rospy.Publisher('game_controller', String, queue_size=10)
    rospy.init_node('game_controller', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "toc %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass