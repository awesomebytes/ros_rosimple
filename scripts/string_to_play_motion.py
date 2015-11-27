#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from play_motion_msgs.msg import PlayMotionActionGoal

class StringToPlayMotion(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/rosimple_string', String, self.sub_cb, queue_size=1)
        self.pub = rospy.Publisher('/play_motion/goal', PlayMotionActionGoal, queue_size=1)

    def sub_cb(self, msg):
        rospy.loginfo("Got msg: " + str(msg))
        g = PlayMotionActionGoal()
        g.goal.motion_name = msg.data
        self.pub.publish(g)
        rospy.loginfo("Publishing goal in play motion: " + str(g))


if __name__ == '__main__':
    rospy.init_node('string_to_play_motion')
    stpm = StringToPlayMotion()
    rospy.spin()
    