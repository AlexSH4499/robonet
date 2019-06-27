#!/usr/bin/env python
import sys,os,inspect
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
params = [ "uid","robot_to_send","executed",'joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
class CustomListener(Leap.Listener):

    def __init__(self):
        self.i = 11
        super(CustomListener, self).__init__()
        self.buffer = []
        return

    def on_init(self, controller):
        print( "Initialized")
        self.clamp = 0

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
        values = [self.i , 1 , False]

        for val in position:
            values.append(str(round(val,2)))
        data = OrderedDict(zip(params,values))
        if len(self.buffer) >= FRAME_BUFFER_LIM:
            print("Entered The BUFFER LOGiC\n\n\n")
            # with open("BUFFERED.txt","a+") as f:
            #     st = str(avg) + '\n'
            #     f.write(st)
            resp = send_response(uid=self.i, data=data)
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
        print( "Connected")
        # Enable gestures
#        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
 #       controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
  #      controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
   #     controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        start = time.time()
        frame = controller.frame()
        hand_props = []
        if(len(frame.hands)!=0 and len(frame.hands)!=2):
            # Get the most recent frame and report some basic information
            #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

            if not frame.hands.is_empty:
                # Get the first hand
                hand = frame.hands[0]
                x,y,z, pitch, yaw, roll = hand_properties(frame)
                print(x,y,z,pitch,yaw,roll)
                # print(len(hand.palm_position))


                hand_props.append(x)
                hand_props.append(y)
                hand_props.append(z)
                hand_props.append(pitch* Leap.RAD_TO_DEG)# x rotation degrees
                hand_props.append(yaw* Leap.RAD_TO_DEG)#y rotation degrees
                hand_props.append(roll* Leap.RAD_TO_DEG)# z rotation degrees
                #print(hand_properties)

                MIN_SPEED=20.0
                MAX_SPEED=80.0

                #IMPORTANT: Face green light toward you.
                left_right_velocity = hand.palm_velocity[0] #right:+ #left:- #
                if abs(left_right_velocity) < MIN_SPEED or abs(left_right_velocity) > 500:
                    adjusted_lrv = 0.0
                elif(left_right_velocity >= MAX_SPEED):
                    adjusted_lrv = 1.0
                elif (left_right_velocity <= -MAX_SPEED):
                    adjusted_lrv = -1.0
                else:
                    adjusted_lrv = left_right_velocity / MAX_SPEED #adjusted lrv
                if adjusted_lrv != 0:
                    motor4="4%f\n" % (adjusted_lrv)
                    #s.send(motor4)  #//////////////////////////////////////////////////////////////////////// LEFT-RIGHT
                    #print(motor4)

                # up is harder than down
                # moving up + down should have higher min speed?
                up_down_velocity = hand.palm_velocity[1] #up:+ #down:-
                if abs(up_down_velocity) < MIN_SPEED or abs(up_down_velocity) > 500:
                    adjusted_udv = 0.0
                elif(up_down_velocity >= MAX_SPEED):
                    adjusted_udv = 1.0
                elif(up_down_velocity <= -MAX_SPEED):
                    adjusted_udv = -1.0
                else:
                    adjusted_udv = up_down_velocity / MAX_SPEED     #adjusted udv
                if adjusted_udv != 0:
                    #motor2="2%f\n" % (adjusted_udv * (-1/4.0)) #might be positive !~!~!~!~!~!~!~!~~!~!~!~!~!
                    motor2="2%f\n" % (adjusted_udv * (3/4.0))
                    #s.send(motor2)  #//////////////////////////////////////////////////////////////////////// UP-DOWN
                    print(motor2)

                forward_back_velocity = -hand.palm_velocity[2] #back:- #frwd:+
                #print "forward back: %f" % forward_back_velocity
                if abs(forward_back_velocity) < MIN_SPEED or abs(forward_back_velocity) > 500:
                    adjusted_fbv = 0.0
                elif(forward_back_velocity >= MAX_SPEED):
                    adjusted_fbv = 1.0
                elif(forward_back_velocity <= -MAX_SPEED):
                    adjusted_fbv = -1.0
                else:
                    adjusted_fbv = forward_back_velocity / MAX_SPEED #adjusted fbv
                if adjusted_fbv != 0:
                    #motor2="2%f\n" % (adjusted_fbv * (1.0/4.0)) #may not work! probably will ~!~!~!~!~!~~~!!~
                    motor3="3%f\n" % (adjusted_fbv * (3.0/4.0))
                    #s.send(motor3)  #//////////////////////////////////////////////////////////////////////// FRWD-BACK
                    #print(motor3)



                # Check if the hand has any fingers
                fingers = hand.fingers
                CLAMP_TIME = 30
                if (len(fingers))>1:
                    # Calculate the hand's average finger tip position
                    self.clamp=max(0, self.clamp - 1)
                    motor0 = "0%f\n" % (-0.5) #////////////////////////////////////////////////////////// OPEN
                    if self.clamp > 0:
                        #s.send(motor0)
                        #print(motor0)
                        pass
                else:
                    self.clamp=min(CLAMP_TIME, self.clamp + 1)
                    motor0="0%f\n" % (0.5) #////////////////////////////////////////////////////////// CLOSE
                    if(self.clamp < CLAMP_TIME):
                        #s.send(motor0)
                        #print(motor0)
                        pass



                # # Get the hand's sphere radius and palm position
                # print("Hand sphere radius: %f mm, palm position: %s" % (
                #       hand.sphere_radius, hand.palm_position))

                # Get the hand's normal vector and direction
                normal = hand.palm_normal
                direction = hand.direction

                # Calculate the hand's pitch
                # print("Hand pitch: %f degrees" % (direction.pitch * Leap.RAD_TO_DEG)) #-20 to 20, ignore -10 to 10
                hand_pitch = direction.pitch * Leap.RAD_TO_DEG
                if (hand_pitch > 10) and (hand_pitch) < 25:
                    motor1 = "1%f\n" % (0.4) #////////////////////////////////////////////////////////// WRIST UP
                    #s.send(motor1)
                    #print(motor1)
                elif(hand_pitch > -20) and (hand_pitch < -10):
                    motor1 = "1%f\n" % (-0.4) #///////////////////////////////////////////////////////// WRIST DOWN
                    #s.send(motor1)
                    #print(motor1)

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
