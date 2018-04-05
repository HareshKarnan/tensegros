#kalman filter implementation to sense the velocities of the nodes and their positions
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # do stuff here with the data

def listener():
    rospy.init_node('raw_sensor_data_listener',anonymous = False)
    rospy.Subscriber("")
