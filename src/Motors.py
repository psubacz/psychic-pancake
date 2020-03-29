import sys, time
import Navio2.Python.navio.pwm 
import Navio2.Python.navio.util as util


class Motor():
    def __init__(self,motorID='', pin = None, pwm_output = 0, period = 50):

        util.check_apm()

        #Motor ID string
        self.ID = motorID
        #Physical hardware pin
        self.pin = pin
        #Output pulse width modulation signal
        self.pwm_output = pwm_output
        #motor pwm attributes
        self.min_pwm = 1.250 #ms
        self.max_pwm = 1.750 #ms

        # self.pwm = Navio2.Python.navio.pwm.PWM(self.pin)
        # self.pwm.set_period(period)
        # self.pwm.enable()

    def write_motor(self,signal):
        # if (signal > self.max_pwm):
        #     self.pwm_output = self.max_pwm
        # elif ((signal < self.min_pwm)):
        #     self.pwm_output = self.min_pwm
        # else:
        #     pass
        # self.pwm.set_duty_cycle(self.pwm_output)
        pass