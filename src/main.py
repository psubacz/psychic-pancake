import rospy, time
from std_msgs.msg import String
# import hardware_interface
# import game_controller
import multiprocessing as mp

class Clockwork_Core(object):
    def __init__(self):
        #---ROS Node
        rospy.init_node('clockwork_core', anonymous=True)
        
        #start subsystems
        # self.start_subsystem()
    
        #---ROS Subscribers
        #sub to the gamepad controller node
        self.g_controller_sub = rospy.Subscriber("hardware_interface", String, self.callback1)
        #sub to the hardware interface node
        self.h_interface_sub = rospy.Subscriber("game_controller", String, self.callback2)
        

    def callback1(self, data):
        # print(data)
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def callback2(self, data):
        # print(data)
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def Run(self):
        # while True: 
        #     print('here')
        # # rospy.spin()
        pass

    
def system_init():
    # 
    pass

def main():
    # jobs = []

    CC = Clockwork_Core()
    # cw_proc = mp.Process(target = CC.Run(),name='GC process')
    # # gc_proc = mp.Process(target = game_controller.talker(),name='GC process')
    # # hi_proc = mp.Process(target = hardware_interface.hi_talker(),name='GC process')
    
    # # jobs.append(cw_proc,gc_proc,hi_proc)
    # print('starting process')
    # hi_proc.start()
    # gc_proc.start()
    # cw_proc.start()
    # cw_proc.join()
    # gc_proc.join()
    # hi_proc.join()
    # Clockwork_Core()
    if not rospy.is_shutdown():
        rospy.spin()

if __name__ == '__main__':
    main()
#clockwork_quadrotor