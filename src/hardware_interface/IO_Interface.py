#!/usr/bin/env python
import sys, time,rospy
import IMU, Led, Motors

class IO_Interface(object):
    '''
    Hardware Interface class that allows control over hardware assets.
    '''
    def __init__(self):
        rospy.init_node('IO_Interface', anonymous=False)
        # pub = rospy.Publisher('IO_Interface/', String, queue_size=10)

        #create motors
        self.motor_1 = Motors.Motor(motorID='t1', pin = 1, pwm_output = 0)
        self.motor_2 = Motors.Motor(motorID='t2', pin = 2, pwm_output = 0)
        self.motor_3 = Motors.Motor(motorID='t3', pin = 3, pwm_output = 0)
        self.motor_4 = Motors.Motor(motorID='t4', pin = 4, pwm_output = 0)

        #create inu sensors
        self.mpu = IMU.Inertia_Measurement_Unit('mpu')
        self.lsm = IMU.Inertia_Measurement_Unit('lsm')
        
        #create led output
        self.led = Led.Navio2_LED()

    def run(self):
            self.mpu.query_sensor()
            self.lsm.query_sensor()

    def set_motor_pwm(self,signal):
        self.motor_1.write_motor(signal)
        self.motor_2.write_motor(signal)
        self.motor_3.write_motor(signal)
        self.motor_4.write_motor(signal)

if __name__ == '__main__':
    #Check to see if roscore is running
    if rospy.is_shutdown():
        print('roscore is not running, please start roscore...')    
    else:
        #
        # navio.util.check_apm()
        #
        interface = IO_Interface()
        #
        while not rospy.is_shutdown():
            #
            interface.run()