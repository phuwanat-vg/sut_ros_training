#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int16

class simpleSubscriber:
    def __init__(self):
        self.number_sub = rospy.Subscriber('integer', Int16, self.num_callback)

    def num_callback(self, msg_in):
        print(msg_in)

def main():
    rospy.init_node('subscriber_node', anonymous = True)
    ss = simpleSubscriber()

    rospy.spin()

if __name__ == "__main__":
    main()
