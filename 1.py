#!/usr/bin/env python

"""Measures the distance travelled by a vehicle in self-driving (auto) mode"""

import rospy
import math
import requests
import time

from fb_tools.path import converter
from protocol.msg import Localization, Topic
from std_msgs.msg import ByteMultiArray


class Odometer(object):
    __slots__ = ['value', 'prev_lat', 'prev_lng', 'is_auto',
                 '_backoff', '_next_submittion', '_endpoint']
    DEFAULT_BACKOFF = 1.0
    SUBMIT_THRESHOLD = 10.0

    def __init__(self, endpoint):
        self.value = 0.0
        self.prev_lat = None
        self.prev_lng = None
        self.is_auto = False
        self._backoff = DEFAULT_BACKOFF
        self._next_submittion = 0.0
        self._endpoint = endpoint

    def subscribe(self):
        rospy.Subscriber(name=Topic.kStateControl, data_class=ByteMultiArray,
                         callback=self.state_control_callback, queue_size=1)
        rospy.Subscriber(name=Topic.kLocalizationFull, data_class=Localization,
                         callback=self.localization_callback, queue_size=1000)

    def localization_callback(self, loc_msg):
        lgo = loc_msg.global_orientation
        lat = loc_msg.latitude
        lng = loc_msg.longitude
        if self.prev_lat is not None and self.prev_lng is not None and self.is_auto:
            self.value += math.sqrt((self.prev_lat - lat) ** 2 + 
                                    (self.prev_lng - lng) ** 2)
        self.prev_lat = lat
        self.prev_lng = lng
        if self.value > SUBMIT_THRESHOLD:
            self.submit()

    def state_control_callback(self, ctrl_msg):
        control = converter.convert_control(ctrl_msg)
        self.is_auto = bool(control.ControlSwitchOn())

    def submit(self):
        if time.time() < self._next_submittion:
            return

        self._next_submittion = time.time() + self._backoff

        try:
            resp = requests.post(self._endpoint, json={value: self.value}, timeout=1)
            resp.raise_for_status()
            self._backoff = Odometer.DEFAULT_BACKOFF
            self.value = 0.0
        except requests.exceptions.RequestException:
            rospy.logerr('Unable to send auto odometer value')
            if self._backoff < 16:
                self._backoff *= 2
            self._next_submittion += self._backoff

def main():
    rospy.init_node(name='auto_odometer')

    odometer = Odometer(rospy.get_param('~endpoint'))
    odometer.subscribe()

    rospy.spin()


if __name__ == '__main__':
    main()