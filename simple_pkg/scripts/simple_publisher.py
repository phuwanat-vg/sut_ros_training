#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int16

class simplePublisher:
    def __init__(self):
        self.number_pub = rospy.Publisher('integer', Int16, queue_size = 5)
        self.num = 0
        period = rospy.Duration(0.1)
        self.timer1 = rospy.Timer(period, self.timer1_callback)
    def number_publish(self):
        if self.num < 1000:
            self.num += 1
        num_msg = Int16()
        num_msg.data = self.num
        self.number_pub.publish(num_msg)
    def timer1_callback(self, event):
        self.number_publish()

def main():
    rospy.init_node('python_simple_pub_node', anonymous = False)
    sp = simplePublisher()
    rospy.spin()

if __name__=="__main__":
    main()







