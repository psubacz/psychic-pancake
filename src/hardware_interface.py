#!/usr/bin/env python
import sys, time
import Navio2.Python.navio.leds as leds
import Navio2.Python.navio.util as util

import Motors

# util.check_apm()
# led = leds.Led()


class Hardware_Interface(object):
    '''
    Hardware Interface class that allows control over hardware assets.
    '''
    def __init__(self):
        self.motor_1 = Motors.Motor(motorID='t1', pin = 1, pwm_output = 0)
        self.motor_2 = Motors.Motor(motorID='t2', pin = 2, pwm_output = 0)
        self.motor_3 = Motors.Motor(motorID='t3', pin = 3, pwm_output = 0)
        self.motor_4 = Motors.Motor(motorID='t4', pin = 4, pwm_output = 0)
        pass

    def change_led(self):
        while (True):
            # led.setColor('Green')
            print ("LED is green")
            time.sleep(1)

            # led.setColor('Red')
            print ("LED is red")
            time.sleep(1)
            break

    def set_motor_pwm(self,signal):
        self.motor_1.write_motor(signal)
        self.motor_2.write_motor(signal)
        self.motor_3.write_motor(signal)
        self.motor_4.write_motor(signal)
        