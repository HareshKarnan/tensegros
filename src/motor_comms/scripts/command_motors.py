#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from serial import *
from math import *
ser = Serial(port='/dev/ttyACM0',baudrate=115200,bytesize=EIGHTBITS,parity=PARITY_NONE,stopbits=STOPBITS_ONE)

def callback(data):
    # do stuff with the data
    # ang2inch =  360.0/(pi*0.395**2)
    ang2inch = 1
    rospy.loginfo('motor1 data received : ' + str(ang2inch*data.data[0]))
    rospy.loginfo('motor2 data received : ' + str(ang2inch*data.data[1]))
    rospy.loginfo('motor3 data received : ' + str(ang2inch*data.data[2]))
    rospy.loginfo('motor4 data received : ' + str(ang2inch*data.data[3]))
    rospy.loginfo('motor5 data received : ' + str(ang2inch*data.data[4]))
    rospy.loginfo('motor6 data received : ' + str(ang2inch*data.data[5]))
    while (ser.isOpen()):
        string = '5:' + str(ang2inch*(-data.data[0])) + ';'
        ser.write(string)
        string = '1:' + str(ang2inch*(data.data[1])) + ';'
        ser.write(string)
        string = '6:' + str(ang2inch*data.data[2]) + ';'
        ser.write(string)
        string = '2:' + str(ang2inch*(-data.data[3])) + ';'
        ser.write(string)
        string = '3:' + str(ang2inch*(data.data[4])) + ';'
        ser.write(string)
        string = '4:' + str(ang2inch*(-data.data[5])) + ';'
        ser.write(string)
        break



def listener():
    rospy.init_node('motors_listener',anonymous = False)
    rospy.Subscriber('motors_command',Float32MultiArray,callback)
    # keep python from exiting
    rospy.spin()

if __name__== '__main__':
    listener()