import sys, time
import navio.pwm 
import navio.util as util


class Motor():
    def __init__(self,motorID='', pin = None, pwm_output = 0, period = 50):

        # self.imu_pub = rospy.Publisher('/'+imu,Float64MultiArray, queue_size=10)

        util.check_apm()
        #Motor ID string
        self.ID = motorID
        #Physical hardware pin
        self.pin = pin
        #motor pwm attributes
        self.min_pwm = 1.250 #ms
        self.max_pwm = 1.750 #ms

        if pwm_output < self.min_pwm or pwm_output > 1.750:
            #Output pulse width modulation signal
            self.pwm_output = pwm_output

        self.pwm = navio.pwm.PWM(self.pin)
        self.pwm.set_period(period)
        self.pwm.enable()

    def write_motor(self,signal):
        #Convert torques to PWM
        signal = self.torque_2_pwm(signal)
        if (signal > self.max_pwm):
            self.pwm_output = self.max_pwm
        elif ((signal < self.min_pwm)):
            self.pwm_output = self.min_pwm
        else:
            pass
        self.pwm.set_duty_cycle(self.pwm_output)
        pass

    def torque_2_pwm(self,signal):
        return signal
