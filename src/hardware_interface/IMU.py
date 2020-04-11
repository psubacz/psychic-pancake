#!/usr/bin/env python
# -*- coding: utf-8 -*-

import navio.mpu9250
import navio.lsm9ds1
import navio.util
from time import sleep
import rospy
from std_msgs.msg import Float64MultiArray

class Inertia_Measurement_Unit(object):
    def __init__(self,imu):
        '''
        Inertia Measurement Unit objects of the NAVIO2 daughter card.
        '''
        
        if imu == 'mpu':
            self.imu = navio.mpu9250.MPU9250()
        elif imu == 'lsm':
            self.imu = navio.lsm9ds1.LSM9DS1()    
        else:
            pass

        self.imu_pub = rospy.Publisher('/'+imu,Float64MultiArray, queue_size=10)
        self.imu.initialize()
        sleep(1)

    def query_sensor(self):        
            m9a, m9g, m9m = self.imu.getMotion9()
            self.imu_pub.publish(data = [float(m9a[0]),float(m9a[1]),float(m9a[2]),
                                        float(m9g[0]),float(m9g[1]),float(m9g[2]),
                                        float(m9m[0]),float(m9m[1]),float(m9m[2])])