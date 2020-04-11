#!/usr/bin/env python
# -*- coding: utf-8 -*-
import navio.leds
import navio.util
from time import sleep
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

class Navio2_LED(object):
    def __init__(self,default_color = 'Yellow'):
        '''
        LED objects of the NAVIO2 daughter card. Status LED is used to encode
         different meanings that are published from differnt nodes

        Creates a 
         system_status 
          5 : Green


        '''
        self.status_dict = {0: 'Red', 
                       1: 'Yellow',
                       2: 'Green',
                       3: 'Blue',
                       4: 'Cyan',
                       5: 'Magenta'}

        self.led = navio.leds.Led()
        self.led_sub = rospy.Subscriber("/set_led", Int8, self.led_cb)
        self.led_pub = rospy.Publisher("/led_color",String, queue_size=10)
        
    def led_cb(self,msg):
        self.led.setColor(self.status_dict[msg])
        self.led_pub.publish(self.status_dict[msg])
        sleep(1)
