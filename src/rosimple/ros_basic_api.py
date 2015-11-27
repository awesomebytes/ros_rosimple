#!/usr/bin/env python

# This file contains functions to execute simple stuff
# to be called by the frontend in an shorter and easier way
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

global TWIST_PUBLISHER
global STRING_PUBLISHER
STRING_PUBLISHER = None
TWIST_PUBLISHER = None
VEL_TOPIC = '/key_vel'
STRING_TOPIC = '/rosimple_string'
RATE = 10

# Move with Twist
def move_twist(direction, seconds):
	"""Move in a direction given seconds"""
	global TWIST_PUBLISHER
	t = Twist()
	if direction.startswith('f'):
		t.linear.x = 0.5
	elif direction.startswith('b'):
		t.linear.x = -0.25
	elif direction.startswith('r'):
		t.angular.z = -0.5
	elif direction.startswith('l'):
		t.angular.z = 0.5


	# This call does nothing if it was already initialized
	try:
		rospy.init_node('rosimple_generated_node', anonymous=True)
	except rospy.exceptions.ROSException:
		pass

	if TWIST_PUBLISHER is None:
		TWIST_PUBLISHER = rospy.Publisher(VEL_TOPIC, Twist, queue_size=1)

	start_time = rospy.Time.now()
	r = rospy.Rate(RATE)
	while not rospy.is_shutdown() and (rospy.Time.now() - start_time) < rospy.Duration(seconds):
		TWIST_PUBLISHER.publish(t)
		r.sleep()


def move_forward(seconds):
	move_twist('forward', seconds)

def move_backward(seconds):
	move_twist('backward', seconds)

def move_right(seconds):
	move_twist('right', seconds)

def move_left(seconds):
	move_twist('left', seconds)


# Publish string
def publish_string(text):
	global STRING_PUBLISHER
	# This call does nothing if it was already initialized
	try:
		rospy.init_node('rosimple_generated_node', anonymous=True)
	except rospy.exceptions.ROSException:
		pass

	if STRING_PUBLISHER is None:
		STRING_PUBLISHER = rospy.Publisher(STRING_TOPIC, String, queue_size=1, latch=True)
	rospy.loginfo("Publishing: " + str(text))
	STRING_PUBLISHER.publish(String(text))
	rospy.loginfo("Published on: " + str(STRING_PUBLISHER.resolved_name))
	if STRING_PUBLISHER.get_num_connections() == 0: # If no one is to listen... wait a moment
		rospy.sleep(1.0)

# Publish integer

# Publish float
