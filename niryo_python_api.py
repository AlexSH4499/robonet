from niryo_one_python_api.niryo_one_api import *
import rospy
import time
#rospy.init_node('niryo_one_example_python_api')

class RobotSession:

    def __init__(self, name='', id=0):
        rospy.init_node('niryo_one_example_python_api')
        self.niryo = NiryoOne()
        self.name = name
        self.id = id

        print('Commencing calibration...')
        self.niryo.calibrate_auto()
        print('Calibration Finished\n\n')
        return

    def __str__(self):
        str = f'[{self.id}]: {self.name}'
        return str

    def run(self):
        try:
            print()
        except NiryoOneException as e:
            print(e)

        finally:
            print("Session Terminated...\n")
        return
