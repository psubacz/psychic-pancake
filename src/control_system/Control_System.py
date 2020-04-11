#!/usr/bin/env python
import sys, time, rospy
import numpy as np
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
from gazebo_msgs.srv import GetWorldProperties, GetModelProperties, GetModelState
from std_msgs.msg import String, Header
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import Point, Pose, PoseArray

class Control_Systems():
    '''
    '''
    def __init__(self):

        self.rostime = lambda: rospy.Time.now().to_sec()

        #--- Initialize
        self.reset()

    def reset(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.m = 0.1            #kg
        self.Ixx = 0.00062      #kg-m^2
        self.Iyy = 0.00113      #kg-m^2
        self.Izz = 0.9*(self.Ixx + self.Iyy) #kg-m^2 (Assume nearly flat object, z=0)
        self.dx = 0.114         #m
        self.dy = 0.0825        #m
        self.g = 9.81998        #m/s**2
        self.DTR = 1/57.3
        self.RTD = 57.3


    def update_model(self):
        pass

    def dynamics_model(self):
        pass