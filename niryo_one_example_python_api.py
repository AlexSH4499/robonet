#!/usr/bin/env python

import time
import json
import requests


from niryo_one_python_api.niryo_one_api import *
from LeapResponse import API_CALL_HANDLER
import rospy


#API ADDRESS
API_ROOT = 'http://192.168.1.29:8000/requests/'#works as tested on Niryo robot
#ask for data by maintaining a request open


def open_connection_to_API(api=API_ROOT):
    session = requests.Session()
    session.verify = True
    req = session.get(api)
    return req

def cleanse_data(req):
    data = req.json()
    for entry in data:#Each entry is an Ordered Dictionary Object
        entry.pop('uid')
        entry.pop('executed')
        entry.pop('robot_to_send')
    return data

def extract_movement(data={}):
    movement = [float(v)  for k,v in sorted(data.items())]
    return movement

def movements(json_data=[]):
    moves = [ extract_movement(data=entry) for entry in json_data]

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
        print(n.get_hardware_status())
        n.set_arm_max_velocity(100)
        n.move_pose(movement)

    except NiryoOneException as e:
        print(e)

    finally:
        print("Niryo Session Terminated\n")
    return

def previous_debug():
    try:
        rospy.init_node('niryo_one_example_python_api')
        n = NiryoOne()
        #n.calibrate_auto()
        #original_data = open_connection_to_API()
        while True:
            print("\nCommencing cycle of requests...\n")
            original_data = open_connection_to_API()
            json_data = cleanse_data(original_data)

            moves = movements(json_data=json_data)

            if len(moves) <= 0 :
                time.sleep(.500)
                continue

            try:

                n.set_arm_max_velocity(100)
                for idx,move in enumerate(moves):
                    print('[{}]move:{}'.format(idx,move))
                    n.move_joints(move)
                    time.sleep(.125)

            except NiryoOneException as e:
                print(e)
                print("Calibrating robot\n\n")
                #n.calibrate_auto()

            finally:
                #mark all requests as processed
                for data in original_data.json():
                    #data['executed'] = True
                    #update database
                    # requests.put(API_ROOT + str(data['uid']) + '/',
                    #                     data=data,auth=('mec123','mec123'))
                    requests.delete(API_ROOT + str(data['uid']) + '/',
                                    auth=('mec123','mec123'))
                json_data = []
                original_data = []
        
                print(original_data)
                print(json_data)
    except KeyboardInterrupt:
        print("Niryo Session Terminated\n\n")
        

def debugging(server_ip, server_port, api_point, username,passw):

    with API_CALL_HANDLER(ip=server_ip, port=server_port, api=api_point, user=username, passw=passw) as API:
        try:
            rospy.init_node('niryo_one_example_python_api')
            n = NiryoOne()
            while True:
                print("\nCommencing cycle of requests...\n")
                original_data = open_connection_to_API(API.api_url())
                json_data = cleanse_data(original_data)

                moves = movements(json_data=json_data)

                if len(moves) <= 0 :
                    time.sleep(.500)
                    continue

                try:

                    n.set_arm_max_velocity(100)
                    for idx,move in enumerate(moves):
                        print('[{}]move:{}'.format(idx,move))
                        n.move_joints(move)
                        time.sleep(.125)

                except NiryoOneException as e:
                    print(e)
                    print("Calibrating robot\n\n")
                    #n.calibrate_auto()

                finally:
                    #delete all requests as processed
                    for data in original_data.json():
                        requests.delete(API.api_url() + str(data['uid']) + '/',
                                        auth=(username,passw))
                    json_data = []
                    original_data = []
            
                    print(original_data)
                    print(json_data)
        except KeyboardInterrupt:
            print("Niryo Session Terminated\n\n")
        
    return

if __name__ == "__main__":
    #main()
    debugging(server_ip='192.168.1.45', server_port='8000', api_point='requests', username='mec123',passw='mec123')
