import time

from niryo_one_python_api.niryo_one_api import *

import numpy
from requests import Session, Request
import rospy

J1_LOWER_LIM = -3.053#rads
J2_LOWER_LIM = -1.919
J3_LOWER_LIM = -1.396
J4_LOWER_LIM = -3.053
J5_LOWER_LIM = -1.744
J6_LOWER_LIM = -2.573

J1_UPPER_LIM = 3.053#rads
J2_UPPER_LIM = 0.639
J3_UPPER_LIM = 1.57
J4_UPPER_LIM = 3.053
J5_UPPER_LIM = 1.919
J6_UPPER_LIM = 2.573

#rospy.init_node('niryo_one_example_python_api')
DEFAULT_ADDRESS = '10.10.10.10'
class RobotSession:

    def __init__(self, name='', id=0, r_ip_address=DEFAULT_ADDRESS):
        rospy.init_node('niryo_one_example_python_api')
        self.niryo = NiryoOne()
        self.name = name
        self.id = id
        self.r_ip_address = r_ip_address
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

    def movement_limits(self):
        restrictions = (,)# restrictions on (x,y,z) & (pitch, roll, yaw)

        return restrictions

    def listen_for_movement(self, src=''):
        request = requests.get(src, stream=True)#Requests cannot release the connection back to the pool unless you consume all the data or call Response.close.

    def send_movement_robot(self,movement=[]):
        if movement is None:
            return None
        elif len(movement) > 6:
            raise ValueError()
        elif len(movement) < 6:
            while len(movement) < 6:
                movement.append(0.0)#pad with 0's
        else:
            request = requests.post(self.r_ip_address, data=movement)

            return request

    def on_error(self):
        print(self.robot_status())
        return

    def init_connection(self, address=DEFAULT_ADDRESS):
        #make a port available for session to listen
        #Open a connection to robot
        request = self.session.get(address, verify=False)#ignores SSL certificate
        return

    def terminate_connection(self):
        #Destroy NiryoObject
        #terminate HTTP connection to Robot port
        self.niryo.wait(time=5)#seconds
        return

    def current_pose(self):
        return self.niryo.get_pose()

    def movement(self, joints=[], arm_vel=100):
        self.niryo.set_max_velocity(arm_vel)
        self.niryo.move_joints(joints)#moves joints to specified position
        #self.niryo.shift_pose(joints)#will take a position relative to current position
        return

    def robot_status(self):
        return self.niryo.get_hardware_status()

    def debug(self):
        print(self.robot_status())

    def __enter__(self,HTTP_REQ):
        '''This will receive a request with robot id, name,ip_address, command and data if any.'''
        try:
            pass
        except NiryoOneException as e:
            self.on_error()
            print(e)
        finally:
            self.terminate_connection()

        return self

    def __exit__(self):
        self.terminate_connection()

        return self

import unittest

class SessionTest(unittest.TestCase):

    def test_robot_connection(self):
        pass

    def test_robot_movement(self):
        pass

    def test_calibration(self):
        pass
