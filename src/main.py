import rospy
from std_msgs.msg import String
import hardware_interface
import game_controller

class Clockwork_Core(object):
    def __init__(self):
        #---ROS Node
        node = rospy.init_node('clockwork_core', anonymous=True)
        
        #start subsystems
        self.start_subsystem()


        #---ROS Subscribers
        #sub to the gamepad controller node
        self.g_controller_sub = rospy.Subscriber("hardware_interface", String, self.callback)
        #sub to the hardware interface node
        self.h_interface_sub = rospy.Subscriber("game_controller", String, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def start_subsystem(self):
        hardware_interface.talker()
        game_controller.talker()

    
def system_init():
    # CC = 
    pass

def main():
    Clockwork_Core()
    if not rospy.is_shutdown():

        rospy.spin()


if __name__ == '__main__':
    main()
#clockwork_quadrotor