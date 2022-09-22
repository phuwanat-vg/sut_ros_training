#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class turtleControl:
    def __init__(self):
        self.vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)
        self.pose_sub = rospy.Subscriber('turtle1/pose', Pose, self.pose_callback)
        per = rospy.Duration(0.1)
        self.timer1 = rospy.Timer(per, self.timer1_callback)
    
    def pose_callback(self, pose_in):
        #print(pose_in.theta)
        theta = pose_in.theta
        if theta < 0:
            print("Negative heading")
        elif theta > 0:
            print("Positive Heading")
    
    def robot_control(self):
        w = 1.0 #rad/s

        vel_msg = Twist()
        vel_msg.angular.z = w
        vel_msg.linear.x = 0.5 #m/s
        self.vel_pub.publish(vel_msg)
    def timer1_callback(self, event):
        self.robot_control()

def main():
    rospy.init_node('turtle_control_node', anonymous = False)
    tc = turtleControl()
    rospy.spin()

if __name__=="__main__":
    main()






