#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from serial import *
ser = Serial(port='/dev/ttyACM0',baudrate=115200,bytesize=EIGHTBITS,parity=PARITY_NONE,stopbits=STOPBITS_ONE)

def callback(data):
    # do stuff with the data
    rospy.loginfo('motor1 data received : ' + str(data.data[0]))
    rospy.loginfo('motor2 data received : ' + str(data.data[1]))
    rospy.loginfo('motor3 data received : ' + str(data.data[2]))
    rospy.loginfo('motor4 data received : ' + str(data.data[3]))
    rospy.loginfo('motor5 data received : ' + str(data.data[4]))
    rospy.loginfo('motor6 data received : ' + str(data.data[5]))
    while (ser.isOpen()):
        string = '1:' + str(data.data[0]) + ';'
        ser.write(string)
        string = '2:' + str(-data.data[1]) + ';'
        ser.write(string)
        string = '3:' + str(data.data[2]) + ';'
        ser.write(string)
        string = '4:' + str(-data.data[3]) + ';'
        ser.write(string)
        string = '5:' + str(-data.data[4]) + ';'
        ser.write(string)
        string = '6:' + str(data.data[5]) + ';'
        ser.write(string)
        break



def listener():
    rospy.init_node('motors_listener',anonymous = False)
    rospy.Subscriber('motors_command',Int32MultiArray,callback)
    # keep python from exiting
    rospy.spin()

if __name__== '__main__':
    listener()