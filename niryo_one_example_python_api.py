#/usr/bin/env python
from niryo_one_python_api.niryo_one_api import *
import rospy
import time

def main():
    rospy.init_node('niryo_one_example_python_api')

    try:
        n = NiryoOne()

        n.set_arm_max_velocity(100)
        n.move_pose(0.2,0,0.15,0,0,0)

    except NiryoOneException as e:
        print(e)

    finally:
        print("Niryo Session Terminated\n")
    return

if __name__ == "__main__":
    main()
