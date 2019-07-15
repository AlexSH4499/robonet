#!/usr/bin/env python
import sys,os,inspect
import math

from collections import OrderedDict

'''This Logic is so we can add the LEAP SDK to our PATH/ENVIRONMENT_VARIABLE'''

print(sys.path.insert(0,'C:\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib\\x64'))

#print(sys.path.insert(0,'C:\\Leap_Motion_Developer_Kit_4.0.0+52173\\LeapSDK\\lib'))
print(sys.path.insert(0,'C:\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib'))
#sys.path.insert(0,'C:\\Users\\Test User\\Downloads\\Leap_Motion_SDK_Windows_2.3.1\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib')
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
print(src_dir)
arch_dir = '../lib/x64'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
'''
This should be abstracted and separated into it's own logic and file
'''

import Leap, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from LeapResponse import send_response

FRAME_BUFFER_LIM = 1

def truncate(num, digs):
    return math.trunc(10** digs * num)/ 10**digs

class HandFrame:

    def __init__(self, x,y,z,pitch, yaw,roll):
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        return

    def __str__(self):
        vars = [(k,v) for k,v in self.__dict__]
        return list(vars)

    def __len__(self):
        return 1

class RobotStructure:

    def __init__(self,uid=0, name=""):
        self.uid = uid
        self.name = name
        self._joints = OrderedDict(self.joints_default_position())
        return

    def joints_default_position(self):
        return zip(self.str_joints(), [0.0 for num in range(len([self.str_joints()]))])

    def joints_limits(self):
        num_lims = zip(self.joint_mins(), self.joint_maxs())
        limits = OrderedDict(zip(self.str_joints(), num_lims))
        for k,v in limits.items():
            yield k,v 

    def joints(self):
        return self._joints

    def joint_mins(self):
        mins = [-3.053, -1.919,-1.396,-3.053,-1.744, -2.573]
        for min in mins:
            yield min

    def joint_maxs(self):
        maxs = [3.053, 0.639, 1.57, 3.053, 1.919, 2.573]
        for max in maxs:
            yield max

    def str_joints(self):
        joints_str = ['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
        for joint in joints_str:
            yield joint

    def update_joint(self, updated_joint={}):
        key, value = updated_joint.keys()[0], updated_joint.values()[0]
        value = self.assert_joint_limits( key, value)
        di = {key:value}
        self.joints().update(di)
        return 
    
    def max_of_joint(self, min_max_tuple=tuple()):
        if len(min_max_tuple) > 2 or len(min_max_tuple) < 2:
            raise ValueError("Min Max Tuple was not properly initialized!\n\n")
        return min_max_tuple[1]
    
    def min_of_joint(self, min_max_tuple=tuple()):
        if len(min_max_tuple) > 2 or len(min_max_tuple) < 2:
            raise ValueError("Min Max Tuple was not properly initialized!\n\n")
        return min_max_tuple[0]

    def assert_joint_limits(self, joint, value):
        
        lims = {k:v for k,v in self.joints_limits()}
        max = self.max_of_joint(lims[joint])
        min = self.min_of_joint(lims[joint])

        if value > max:
            return math.floor(truncate(max, digs=2))
        
        if value < min :
            return math.floor(truncate(min, digs=2))

        return value

    def __len__(self):
        return len(self._joints) #should be 6 here but must verify this works

    #we need to fix this, somehow idk...
    def __str__(self):
        str_robot = ['UID:',self.uid,'\t|\tName:',self.name,'\n']
        str_joints = ['|'+str(k)+':' +str(v) + '|\t' for k,v in self.joints()]
        return str(str_robot) + str(str_joints)

class RobotData(OrderedDict):

    def __init__(self, values):

        self.params = ('uid','robot_to_send','executed',
                    'joint_1','joint_2','joint_3',
                    'joint_4','joint_5','joint_6')
        self.values = values
        return
    def __params_to_remove(self):
        return ('uid','robot_to_send','executed',)

    def cleansed_data(self):
        return {k:v
                    for k,v in zip(self.params, self.values)
                     if k not in self.__params_to_remove()}
                     
params = [ 'uid','robot_to_send','executed',
            'joint_1','joint_2','joint_3',
            'joint_4','joint_5','joint_6']

class CustomListener(Leap.Listener):

    def __init__(self):
        self.i = 0
        self.robot = RobotStructure(uid=1 , name="Alpha")
        super(CustomListener, self).__init__()
        self.buffer = []
        return

    def on_init(self, controller):
        print( "Initialized")
        self.clamp = 0

    '''UPDATE THESE VARIABLE NAMES, THEY'RE WRONG!'''
    def averaged_position(self, positions):
        _x,_y,_z,_pitch,_roll,_yaw = 0, 0, 0, 0, 0, 0
        # print(position)
        for x,y,z,pitch,roll,yaw in positions:
            _x += x
            _y += y
            _z += z
            _yaw += yaw
            _roll +=roll
            _pitch += pitch

        if len(positions) > 0:
            _x /= len(positions)
            _y /= len(positions)
            _z /= len(positions)
            _yaw /= len(positions)
            _roll /= len(positions)
            _pitch /= len(positions)
        return _x,_y,_z,_pitch,_roll,_yaw

    def default_data(self):
        robot, executed, uid = self.robot.uid , False, self.i
        values = [uid,robot, executed]
        return values

    def frame_buffer(self,frame):
        position = self.averaged_position(self.buffer)
        values = self.default_data()#= [uid , robot , executed]

        for val in position:
            values.append(str(round(val,2)))

        joint_data = OrderedDict(zip(params,values))#preserve the order of the joints
                                              #otherwise, our RESTAPI breaks due to values getting displaced
        
        if len(self.buffer) >= FRAME_BUFFER_LIM:# length of buffer is or exceeds our global limit
            print("Entered The BUFFER LOGiC\n\n\n")
            # with open("BUFFERED.txt","a+") as f:
            #     st = str(avg) + '\n'
            #     f.write(st)
            resp = send_response(uid=values[0], data=joint_data)#send our averaged data to REST API
            #print(resp.json)
            #print(resp.headers)
            print('Exited\n\n\n\n\n')
            self.i = self.i + 1

            while len(self.buffer) > 0:
                self.buffer.pop()#empty our buffer
        
        self.buffer.append(frame)#add frame to buffer
        avg = self.averaged_position(self.buffer)
        return avg

    def on_connect(self, controller):
        print( "Connected...\n\n")
        # Enable gestures
#        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
 #       controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
  #      controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
   #     controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected\n\n")

    def on_exit(self, controller):
        print("Exited\n\n")

    def on_frame(self, controller):

        frame = controller.frame()
        hand_props = []
        if(len(frame.hands)!=0 and len(frame.hands)!=2):

            if not frame.hands.is_empty:

                str_joints = self.robot.str_joints()
                current_joints =  zip(str_joints, convert_to_joints(hand_properties(frame)))#data received from Leap Motion
                
                for joint, val in current_joints:
                    self.robot.update_joint(updated_joint={joint:val})

                for val in self.robot.joints().values():
                    hand_props.append(val)

            averaged_position = self.frame_buffer(tuple(hand_props))

            #Empty out the props for next frame
            while len(hand_props):
                hand_props.pop()

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

    # def __enter__(self):

    #     return self

    # def __exit__(self):
    #     self.controller.remove_listener(self)
    #     return

def average_direction(directions):
    sum_x= 0
    sum_y = 0
    sum_z = 0

    for dir in directions:
        x,y,z = dir
        sum_x += x
        sum_y += y
        sum_z += z
    
    avg_x = sum_x / len(directions)
    avg_y = sum_y/ len(directions)
    avg_z = sum_z/ len(directions)
    return avg_x, avg_y, avg_z

fingers= []
def hand_properties(frame):

    hand = frame.hands.rightmost

    #Cannot be unpacked due to improper wrapping of tuples and lack of len implementation in Python API
    x = hand.palm_position[0] * (10 ** -3)#convert mm to meters
    y = hand.palm_position[1] * (10 ** -3)#convert mm to meters
    z = hand.palm_position[2] * (10 ** -3)#convert mm to meters
    avg_finger_dir = 1
    finger = hand.fingers[0]
    if len(fingers) < FRAME_BUFFER_LIM:
        fingers.append(finger_properties(finger))

    else:
        #we need to average them out
        avg_finger_dir = average_direction(directions=fingers)
    #print(hand.fingers[0].direction)
    
    velocity = hand.palm_velocity
    normal_vector = hand.palm_normal
    finger_x, finger_y, finger_z = avg_finger_dir
    pitch = hand.direction.pitch# x axis angle
    yaw = hand.direction.yaw# y axis
    roll = hand.palm_normal.roll#z axis relative to normal_vector
    # return position, pitch, yaw, roll
    finger_yaw = 0
    if finger_x != 0:
        finger_yaw = math.atan(finger_y/finger_x)
    
    return x, y, z, pitch, yaw, roll, finger_yaw

def finger_properties(hand):
    '''PROBLEM: For some reason the fingers[0] gives a problem,
    maybe because we have to ensure there exists a finger in the hand to begin with'''
    #print(hand.fingers[0]+'\n')
    #finger_x, finger_y, finger_z = hand.fingers[0].direction
    finger_x, finger_y, finger_z = 0,0,0
    return finger_x, finger_y, finger_z

def convert_to_joints(properties):
    if len(properties)  < 6 :
        raise ValueError("Not a valid property structure!\n\n")

    x,y,z,pitch,yaw,roll, finger_yaw = properties

    if properties[0] != 0:
        y_x_scaling = properties[1] / properties[0]# y / x
    else:
        y_x_scaling = 1
    distance_x_z = math.sqrt(x ** 2 + z**2)
    distance_org = math.sqrt(x ** 2 + y ** 2 +z**2)
    # we should validate that the values are within params
    # joint_1 = roll #joint 1 - base (X-Z axis)

    # joint_2 = pitch#yaw * y_x_scaling #_yaw | main vertical trunk XY rotation
    # joint_3 = finger_yaw # top joint XY plane rotation
    # joint_4 = roll #distance of x-z| X-Z arm
    # joint_5 = pitch #XY plane of hand
    # #joint_5 = roll * distance_x_z#these two are the hand
    # joint_6 = distance_org#this one is wrist rotation

    joint_1 = 0#base motor
    joint_2 = 0.6777#yaw * y_x_scaling #_yaw | main vertical trunk XY rotation
    joint_3 = 0 # top joint XY plane rotation
    joint_4 = 0 #distance of x-z| X-Z arm
    joint_5 = 0 #XY plane of hand
    #joint_5 = roll * distance_x_z#these two are the hand
    joint_6 = 0#this one is wrist rotation

    print("|Hand Properties|\n")
    print("\tX: %f | Y: %f | Z: %f |\n Palm-Pitch: %f | Palm-Yaw: %f | Palm-Roll: %f |\n Finger Yaw:%f|\n\n"%(x,y,z,pitch,yaw,roll, finger_yaw))
    
    print("|Joint Conversions|\n")
    print("\tJ1: %f | J2: %f | J3: %f | J4: %f | J5: %f | J6: %f\n\n"%(x,y,z,pitch,yaw,roll))
    return joint_1,joint_2,joint_3,joint_4,joint_5,joint_6,


def main():

    # Create a sample listener and controller
    listener = CustomListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()

# import unittest

# class RobotTest(unittest.TestCase):

#     def test_len(self):
#         robot = RobotStructure()
#         self.assertTrue(len(robot) == 6)

#     from hypothesis import given
#     from hypothesis.strategies import floats

#     @given(value=floats())
#     def test_lims(self, value, robot=RobotStructure()):
#         assert robot.assert_joint_limits('joint_1', value) == truncate(robot.joints_limits()['joint_1'],2)
       