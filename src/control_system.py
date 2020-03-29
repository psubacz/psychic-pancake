#!/usr/bin/env python
import sys, time, rospy
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler
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

    def control_update(self):
        pass

    def dynamics_model(self):
        pass