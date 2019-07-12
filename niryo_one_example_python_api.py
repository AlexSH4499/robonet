#/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy

import time
import json
import requests

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
    # print(data)
    # print('\n\n')
    for entry in data:#Each entry is an Ordered Dictionary Object
        entry.pop('uid')
        entry.pop('executed')
        entry.pop('robot_to_send')
    return data

def extract_movement(data={}):
    movement = [float(v)  for k,v in sorted(data.items())]
    #for k, v in data: error in Python 2, only works in 3
    # for k,v in sorted(data.iteritems()):
    #     joint = float(v)
    #     movement.append(joint)
    return movement

def movements(json_data=[]):
    moves = [ extract_movement(data=entry) for entry in json_data]
    # for entry in  json_data:
    #     moves.append(extract_movement(data=entry))

    for idx,move in enumerate(moves):
        print('[%d]:%s'%(idx,move))
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
    try:
        rospy.init_node('niryo_one_example_python_api')
        n = NiryoOne()

        while True:
            print("\nCommencing cycle of requests...\n")
            original_data = open_connection_to_API()
            json_data = cleanse_data(original_data)
            # print('Original data:')
            # for idx, entry in enumerate(original_data):
            #     print("[%d]: %s"%(idx,entry))
            # print('\n')

            # print('Json data:')
            # for idx, entry in enumerate(json_data):
            #     print("[%d]: %s"%(idx,entry))
            # print('\n')
            # for entry in  json_data:
            #     print(entry)
            # print('\n\n')

            moves = movements(json_data=json_data)

            if len(moves) <= 0 :
                time.sleep(.500)
                continue

            try:

                n.set_arm_max_velocity(100)
                for move in moves:
                    print(move)
                    n.move_joints(move)
                    time.sleep(.5)

            except NiryoOneException as e:
                print(e)

            finally:
                #mark all requests as processed
                for data in original_data.json():
                    data['executed'] = True
                    #update database
                    requests.put(API_ROOT + str(data['uid']) + '/',
                                        data=data,auth=('mec123','mec123'))
                json_data = []
                original_data = []
        
           
    except KeyboardInterrupt:
        print("Niryo Session Terminated\n\n")
    return

if __name__ == "__main__":
    #main()'
    debugging()
