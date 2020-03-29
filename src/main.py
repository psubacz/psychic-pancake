import rospy, time, sched
from std_msgs.msg import String
import hardware_interface as hardware_interface
import control_system as control_system
# import game_controller
import multiprocessing as mp


'''
Example ROS code:
https://github.com/jnez71/lqRRT/blob/master/demos/lqrrt_ros/nodes/lqrrt_node.py
'''
class Clockwork_Core(object):
    def __init__(self):
        #--- ROS Node
        # Make sure roscore is running 
        # Initialize core node 
        rospy.init_node('clockwork_core', anonymous=True)

        #--- initialize scheduler        
        self.schedule = sched.scheduler(time.time, time.sleep) 

        #--- initialize modules
        self.interface = hardware_interface.Hardware_Interface()
        self.controller = control_system.Control_Systems()

        #--- initialize subscribers
        #sub to the gamepad controller node
        self.g_controller_sub = rospy.Subscriber("game_controller", String, self.callback1)        

        #--- Populate default scheduler
        self.schedule_default()

    def callback1(self, data):
        # print(data)
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def schedule_default(self):
        '''
        Populates the scehedule with priority 1 actions:
        - interface action
        '''
        self.schedule.enterabs(time = time.time(), priority = 1, action = self.interface.change_led)
        self.schedule.enterabs(time = time.time(), priority = 1, action = self.interface.set_motor_pwm)
        self.schedule.enterabs(time = time.time(), priority = 1, action = self.controller.control_update)

    def main(self):
        '''
        Operating loop 
        
        '''
        #while the scheduler is not empty
        while not self.schedule.empty():
            #run scheduled events
            self.schedule.run()
            
            #populate the scheduler with default task
            self.schedule_default()

if __name__ == '__main__':
    if rospy.is_shutdown():
        print('rosok')
        print('roscore is not running, please start roscore...')
        exit()
    else:
        core = Clockwork_Core()
        core.main()