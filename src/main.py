# import rospy, time, sched, json
# from std_msgs.msg import String
# import hardware_interface as hardware_interface
# import control_system as control_system
# # import game_controller
# import multiprocessing as mp

# '''
# Example ROS code:
# https://github.com/jnez71/lqRRT/blob/master/demos/lqrrt_ros/nodes/lqrrt_node.py
# '''
# class Clockwork_Core(object):
#     def __init__(self):
#         #--- ROS Node
#         # Make sure roscore is running 
#         # Initialize core node 
#         rospy.init_node('clockwork_core', anonymous=True)

#         #--- Initialize Scheduler        
#         self.schedule = sched.scheduler(time.time, time.sleep) 

#         #--- Initialize Modules
#         self.interface = hardware_interface.Hardware_Interface()
#         self.controller = control_system.Control_Systems()

#         #--- Initialize Subscribers
#         #sub to the gamepad controller node
#         self.g_controller_sub = rospy.Subscriber("game_controller", String, self.callback1)        

#         #--- Populate default scheduler
#         self.schedule_default()

#     def shutdown(self):
#         pass

#     def callback1(self, data):
#         # print(data)
#         rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

#     def schedule_default(self):
#         '''
#         Populates the scehedule with priority 1 actions (actions that need to be done every loop):
#         - Examples are: 
#         -- interface:
#         --- Change LED signal
#         --- Output PWM signal
#         -- Controller
#         --- Update model based on time step T

#         '''
#         self.schedule.enterabs(time = time.time(), priority = 1, action = self.interface.change_led)
#         self.schedule.enterabs(time = time.time(), priority = 1, action = self.interface.set_motor_pwm)
#         self.schedule.enterabs(time = time.time(), priority = 1, action = self.controller.update_model)

#     def main(self):
#         '''
#         Operating loop that executes scheduled tasks  in a time & priority queue
#         '''
#         #while the scheduler is not empty
#         while not self.schedule.empty():
#             #Run scheduled events
#             self.schedule.run()
            
#             #Populate the scheduler with default task
#             self.schedule_default()

# if __name__ == '__main__':

#     setup_good = True
    
#     if rospy.is_shutdown():
#         #Check to see if roscore is running
#         print('roscore is not running, please start roscore...')      
#         setup_good = False
#     else:
#         pass #do nothing

#     if setup_good:
#         # if there is no errors during startup, instaniate the core and run the main file
#         print('rosok')
#         core = Clockwork_Core()
#         core.main()
#     exit()