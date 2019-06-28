#/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy

import time
import json
import requests

#from samples import LeapResponse.receive_response

#API ADDRESS
API_ROOT = 'http://192.168.1.21:8000/requests/'#works as tested on Niryo robot
#ask for data by maintaining a request open


def open_connection_to_API():
    session = requests.Session()
    session.verify = True
    req = session.get(API_ROOT)
    # print(req.text)
    return req

def cleanse_data(req):
    data = req.json()
    print(data)
    print('\n\n')
    for entry in data:
        entry.pop('uid')
        entry.pop('executed')
        entry.pop('robot_to_send')
    return data

limit = 0.3#placeholder limit
def extract_movement(data={}):
    movement = []
    print(type(data))
    #for k, v in data: error in Python 2, only works in 3
    for m in data.itervalues():
        joint = float(m)
        if joint > limit:
            joint = limit
        if joint < -limit:
            joint = -limit
        movement.append(joint)
    return movement


def movements(json_data=[]):
    moves = []
    for entry in  json_data:
        moves.append(extract_movement(data=entry))

    for move in moves:
        print(move)
    print('\n\n')
    return moves

def dummy_movement():
    return [0.2,0,0.15,0,0,0]

def main():
    rospy.init_node('niryo_one_example_python_api')
    movement= dummy_movement()
    try:
        n = NiryoOne()

        n.set_arm_max_velocity(100)
        n.move_pose(movement)

    except NiryoOneException as e:
        print(e)

    finally:
        print("Niryo Session Terminated\n")
    return

def debugging():
    json_data = cleanse_data(open_connection_to_API())
    for entry in  json_data:
        print(entry)
    print('\n\n')

    moves = movements(json_data=json_data)

    rospy.init_node('niryo_one_example_python_api')
    try:
        n = NiryoOne()

        n.set_arm_max_velocity(100)
        # move =moves[0]
        # print(move)
        for move in moves:
            print(move)
            #n.move_pose(move)
            n.move_joints(move)
            time.sleep(1)



    except NiryoOneException as e:
        print(e)

    finally:
        print("Niryo Session Terminated\n")
    return

if __name__ == "__main__":
    #main()'
    debugging()
