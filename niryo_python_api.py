import time

from niryo_one_python_api.niryo_one_api import *
from requests import Session, Request
import rospy

#rospy.init_node('niryo_one_example_python_api')
DEFAULT_ADDRESS = '10.10.10.10'
class RobotSession:

    def __init__(self, name='', id=0):
        rospy.init_node('niryo_one_example_python_api')
        self.niryo = NiryoOne()
        self.name = name
        self.id = id
        self.session = Session()
        print('Commencing calibration...')
        self.niryo.calibrate_auto()
        print('Calibration Finished\n\n')
        return

    def __str__(self):
        str = f'[{self.id}]: {self.name}'
        return str

    def run(self):
        try:
            print('Starting Session')
            while True:#while connection is alive, keep listening on port

                print(self.name)

        except NiryoOneException as e:
            print(e)

        finally:
            print("Session Terminated...\n")
        return

    def init_connection(self, address=DEFAULT_ADDRESS):
        #make a port available for session to listen
        #Open a connection to robot
        request = self.session.get(address)
        return

    def terminate_connection(self):
        #Destroy NiryoObject
        #terminate HTTP connection to Robot port
        self. niryo.wait(time=5)#seconds
        return

    def current_pose(self):
        return self.niryo.get_pose()

    def movement(self, joints=[], arm_vel=10):
        self.niryo.set_max_velocity(arm_vel)
        self.niryo.move_joints(joints)#moves joints to specified position
        #self.niryo.shift_pose(joints)#will take a position relative to current position
        return

    def robot_status(self):
        return self.niryo.get_hardware_status()

    def debug(self):
        print(self.robot_status())

import unittest


class SessioTest(unittest.TestCase):

    def test_robot_connection(self):
