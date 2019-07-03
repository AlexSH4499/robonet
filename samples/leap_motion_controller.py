#!/usr/bin/env python
import sys,os,inspect
import math

from collections import OrderedDict

print(sys.path.insert(0,'C:\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib\\x64'))

#print(sys.path.insert(0,'C:\\Leap_Motion_Developer_Kit_4.0.0+52173\\LeapSDK\\lib'))
print(sys.path.insert(0,'C:\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib'))
#sys.path.insert(0,'C:\\Users\\Test User\\Downloads\\Leap_Motion_SDK_Windows_2.3.1\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib')
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
print(src_dir)
arch_dir = '../lib/x64'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from LeapResponse import send_response

FRAME_BUFFER_LIM = 60

class HandFrame:

    def __init__(self, x,y,z,pitch, yaw,roll):
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        return self



    def __str__(self):
        vars = [(k,v) for k,v in self.__dict__]
        return list(vars)

    def __len__(self):
        return 1

class RobotStructure:

    def __init__(self, name=""):
        self.name = name
        self.joints = (('joint_1',0.0),('joint_2',0.0),
                        ('joint_3',0.0),('joint_4',0.0),
                        ('joint_5',0.0),('joint_6',0.0),)
    def joints(self):
        for joint in self.joints:
            yield joint

    def __len__(self):
        return len(self.joints) #should be 6 here but must verify this works


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
        super(CustomListener, self).__init__()
        self.buffer = []
        return

    def on_init(self, controller):
        print( "Initialized")
        self.clamp = 0

    '''UPDATE THESE VARIABLE NAMES, THEY'RE WRONG!'''
    def averaged_position(self, frame_list):
        _x,_y,_z,_pitch,_roll,_yaw = 0, 0, 0, 0, 0, 0
        # print(frame_list)
        for x,y,z,pitch,roll,yaw in frame_list:
            _x += x
            _y += y
            _z += z
            _yaw += yaw
            _roll +=roll
            _pitch += pitch

        if len(frame_list) > 0:
            _x /= len(frame_list)
            _y /= len(frame_list)
            _z /= len(frame_list)
            _yaw /= len(frame_list)
            _roll /= len(frame_list)
            _pitch /= len(frame_list)
        return _x,_y,_z,_pitch,_roll,_yaw

    def frame_buffer(self,frame):
        position = self.averaged_position(self.buffer)
        robot = 1
        executed  = False
        uid = self.i
        values = [uid , robot , executed]

        for val in position:
            values.append(str(round(val,2)))
        data = OrderedDict(zip(params,values))#preserve the order of the joints
                                              #otherwise, our RESTAPI breaks due to values getting displaced
        if len(self.buffer) >= FRAME_BUFFER_LIM:
            print("Entered The BUFFER LOGiC\n\n\n")
            # with open("BUFFERED.txt","a+") as f:
            #     st = str(avg) + '\n'
            #     f.write(st)
            resp = send_response(uid=uid, data=data)
            print(resp.json)
            # print(resp.headers)
            print('\n\n\n\n\n')
            self.i = self.i + 1

            while len(self.buffer) > 0:
                self.buffer.pop()

        self.buffer.append(frame)
        avg = self.averaged_position(self.buffer)
        return avg

    def on_connect(self, controller):
        print( "Connected\n\n")
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
        #start = time.time()
        frame = controller.frame()
        hand_props = []
        if(len(frame.hands)!=0 and len(frame.hands)!=2):
            # Get the most recent frame and report some basic information
            #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

            if not frame.hands.is_empty:
                # Get the first hand
                hand = frame.hands[0]
                x,y,z, pitch, yaw, roll = assert_limits(convert_to_joints(hand_properties(frame)))#not really x,y,z anynmore, now its joints
                # print(x,y,z,pitch,yaw,roll)
                # print(len(hand.palm_position))


                hand_props.append(x)
                hand_props.append(y)
                hand_props.append(z)
                # hand_props.append(pitch* Leap.RAD_TO_DEG)# x rotation degrees
                # hand_props.append(yaw* Leap.RAD_TO_DEG)#y rotation degrees
                # hand_props.append(roll* Leap.RAD_TO_DEG)# z rotation degrees
                hand_props.append(pitch)# x rotation rads
                hand_props.append(yaw)#y rotation rads
                hand_props.append(roll)# z rotation rads
                # print(hand_props)

                # MIN_SPEED=20.0
                # MAX_SPEED=80.0
                #
                # #IMPORTANT: Face green light toward you.
                # left_right_velocity = hand.palm_velocity[0] #right:+ #left:- #
                # if abs(left_right_velocity) < MIN_SPEED or abs(left_right_velocity) > 500:
                #     adjusted_lrv = 0.0
                # elif(left_right_velocity >= MAX_SPEED):
                #     adjusted_lrv = 1.0
                # elif (left_right_velocity <= -MAX_SPEED):
                #     adjusted_lrv = -1.0
                # else:
                #     adjusted_lrv = left_right_velocity / MAX_SPEED #adjusted lrv
                # if adjusted_lrv != 0:
                #     motor4="4%f\n" % (adjusted_lrv)
                #     #s.send(motor4)  #//////////////////////////////////////////////////////////////////////// LEFT-RIGHT
                #     #print(motor4)
                #
                # # up is harder than down
                # # moving up + down should have higher min speed?
                # up_down_velocity = hand.palm_velocity[1] #up:+ #down:-
                # if abs(up_down_velocity) < MIN_SPEED or abs(up_down_velocity) > 500:
                #     adjusted_udv = 0.0
                # elif(up_down_velocity >= MAX_SPEED):
                #     adjusted_udv = 1.0
                # elif(up_down_velocity <= -MAX_SPEED):
                #     adjusted_udv = -1.0
                # else:
                #     adjusted_udv = up_down_velocity / MAX_SPEED     #adjusted udv
                # if adjusted_udv != 0:
                #     #motor2="2%f\n" % (adjusted_udv * (-1/4.0)) #might be positive !~!~!~!~!~!~!~!~~!~!~!~!~!
                #     motor2="2%f\n" % (adjusted_udv * (3/4.0))
                #     #s.send(motor2)  #//////////////////////////////////////////////////////////////////////// UP-DOWN
                #     print(motor2)
                #
                # forward_back_velocity = -hand.palm_velocity[2] #back:- #frwd:+
                # #print "forward back: %f" % forward_back_velocity
                # if abs(forward_back_velocity) < MIN_SPEED or abs(forward_back_velocity) > 500:
                #     adjusted_fbv = 0.0
                # elif(forward_back_velocity >= MAX_SPEED):
                #     adjusted_fbv = 1.0
                # elif(forward_back_velocity <= -MAX_SPEED):
                #     adjusted_fbv = -1.0
                # else:
                #     adjusted_fbv = forward_back_velocity / MAX_SPEED #adjusted fbv
                # if adjusted_fbv != 0:
                #     #motor2="2%f\n" % (adjusted_fbv * (1.0/4.0)) #may not work! probably will ~!~!~!~!~!~~~!!~
                #     motor3="3%f\n" % (adjusted_fbv * (3.0/4.0))
                #     #s.send(motor3)  #//////////////////////////////////////////////////////////////////////// FRWD-BACK
                #     #print(motor3)
                #
                #
                #
                # # Check if the hand has any fingers
                # fingers = hand.fingers
                # CLAMP_TIME = 30
                # if (len(fingers))>1:
                #     # Calculate the hand's average finger tip position
                #     self.clamp=max(0, self.clamp - 1)
                #     motor0 = "0%f\n" % (-0.5) #////////////////////////////////////////////////////////// OPEN
                #     if self.clamp > 0:
                #         #s.send(motor0)
                #         #print(motor0)
                #         pass
                # else:
                #     self.clamp=min(CLAMP_TIME, self.clamp + 1)
                #     motor0="0%f\n" % (0.5) #////////////////////////////////////////////////////////// CLOSE
                #     if(self.clamp < CLAMP_TIME):
                #         #s.send(motor0)
                #         #print(motor0)
                #         pass
                #
                #
                #
                # # # Get the hand's sphere radius and palm position
                # # print("Hand sphere radius: %f mm, palm position: %s" % (
                # #       hand.sphere_radius, hand.palm_position))
                #
                # # Get the hand's normal vector and direction
                # normal = hand.palm_normal
                # direction = hand.direction
                #
                # # Calculate the hand's pitch
                # # print("Hand pitch: %f degrees" % (direction.pitch * Leap.RAD_TO_DEG)) #-20 to 20, ignore -10 to 10
                # hand_pitch = direction.pitch * Leap.RAD_TO_DEG
                # if (hand_pitch > 10) and (hand_pitch) < 25:
                #     motor1 = "1%f\n" % (0.4) #////////////////////////////////////////////////////////// WRIST UP
                #     #s.send(motor1)
                #     #print(motor1)
                # elif(hand_pitch > -20) and (hand_pitch < -10):
                #     motor1 = "1%f\n" % (-0.4) #///////////////////////////////////////////////////////// WRIST DOWN
                #     #s.send(motor1)
                #     #print(motor1)

            # print "%f seconds" % (time.time() - start)
            averaged_position = self.frame_buffer(tuple(hand_props))

            #Empty out the props for next frame
            while len(hand_props):
                hand_props.pop()

        # we need to create a buffere here to limit how many requests are made

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

def joint_limits():
    limits = OrderedDict({'joint_1':(-3.053,3.053),'joint_2':(-1.919,0.639),'joint_3':(-1.396,1.57),
                        'joint_4':(-3.053,3.053),'joint_5':(-1.744, 1.919),'joint_6':(-2.573,2.573)})
    return limits

def hand_properties(frame):

    hand = frame.hands.rightmost

    x = hand.palm_position[0] * (10 ** -3)#convert mm to meters
    y = hand.palm_position[1] * (10 ** -3)#convert mm to meters
    z = hand.palm_position[2] * (10 ** -3)#convert mm to meters


    #position = (x,y,z,) #in millimeters
    velocity = hand.palm_velocity
    normal_vector = hand.palm_normal

    pitch = hand.direction.pitch# x axis angle
    yaw = hand.direction.yaw# y axis
    roll = hand.palm_normal.roll#z axis relative to normal_vector
    # return position, pitch, yaw, roll
    return x, y, z, pitch, yaw, roll

def convert_to_joints(properties):
    if len(properties)  is not  6 :
        raise ValueError("Not a valid property structure!\n\n")

    x,y,z,pitch,yaw,roll = properties

    if properties[0] != 0:
        y_x_scaling = properties[1] / properties[0]# y / x
    else:
        y_x_scaling = 1
    distance_x_z = math.sqrt(x ** 2 + z**2)

    # we should validate that the values are within params
    joint_1 = roll #joint 1 - base (X-Z axis)

    joint_2 = pitch#yaw * y_x_scaling #_yaw | main vertical trunk XY rotation
    joint_3 = yaw * y_x_scaling# top joint XY plane rotation
    joint_4 = roll #distance of x-z| X-Z arm
    joint_5 = pitch #XY plane of hand
    #joint_5 = roll * distance_x_z#these two are the hand
    joint_6 = yaw#this one is wrist rotation

    print("X: %f | Y: %f | Z: %f | Palm-Pitch: %f | Palm-Yaw: %f | Palm-Roll: %f"%(x,y,z,pitch,yaw,roll))
    print("J1: %f | J2: %f | J3: %f | J4: %f | J5: %f | J6: %f\n\n"%(x,y,z,pitch,yaw,roll))
    return joint_1,joint_2,joint_3,joint_4,joint_5,joint_6,

#joints = ['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
def assert_limits(converted_joints):

    joint_1,joint_2,joint_3,joint_4,joint_5,joint_6 = converted_joints
    lims = joint_limits()

    #minimums
    if joint_1 < lims['joint_1'][0]:
        joint_1 = lims['joint_1'][0]

    if joint_2 < lims['joint_2'][0]:
        joint_2 = lims['joint_2'][0]

    if joint_3 < lims['joint_3'][0]:
        joint_3 = lims['joint_3'][0]

    if joint_4 < lims['joint_4'][0]:
        joint_4 = lims['joint_4'][0]

    if joint_5 < lims['joint_5'][0]:
        joint_5 = lims['joint_5'][0]

    if joint_6 < lims['joint_6'][0]:
        joint_6 = lims['joint_6'][0]

    #maximums
    if joint_1 > lims['joint_1'][1]:
        joint_1 = lims['joint_1'][1]

    if joint_2 > lims['joint_2'][1]:
        joint_2 = lims['joint_2'][1]

    if joint_3 > lims['joint_3'][1]:
        joint_3 = lims['joint_3'][1]

    if joint_4 > lims['joint_4'][1]:
        joint_4 = lims['joint_4'][1]

    if joint_5 > lims['joint_5'][1]:
        joint_5 = lims['joint_5'][1]

    if joint_6 > lims['joint_6'][1]:
        joint_6 = lims['joint_6'][1]


    return joint_1,joint_2,joint_3,joint_4,joint_5,joint_6

def main():

    # Create a sample listener and controller
    listener = CustomListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    #print "here"
    #sys.exit()
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()

import unittest

class RobotTest(unittest.TestCase):

    def test_len(self):
        robot = RobotStructure()
        self.assertTrue(len(robot) == 6)