import os, sys, inspect, _thread, time
from pathlib import Path, PureWindowsPath

library_dir = PureWindowsPath("leap_motion_lib\\x64")
corrected_path = Path(library_dir)
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
print(src_dir)
# src_dir = os.path.abspath("C:\\Leap_Motion_Developer_Kit_4.0.0+52173\\LeapSDK")
# # Windows and Linux
#arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# # Mac
# #arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
#sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
# print(os.path.abspath(os.path.join(src_dir, '../leap_motion_lib/x64')) )
# print(sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../leap_motion_lib/x64'))) )
#sys.path.append(r"C:\Leap_Motion_Developer_Kit_4.0.0+52173\LeapSDK\lib\x64")
# sys.path.append(r"C:\Leap_Motion_Developer_Kit_4.0.0+52173\LeapSDK")
# sys.path.append(r"C:\Leap_Motion_Developer_Kit_4.0.0+52173\LeapSDK\lib")
# sys.path.append(r"C:\Leap_Motion_Developer_Kit_4.0.0+52173\LeapSDK\lib\x86")
abs_path = os.path.join(src_dir,corrected_path)
print(abs_path)
#sys.path.append( os.path.abspath(os.path.join(src_dir, r'\leap_motion_lib\x64')))

print(sys.path.append(abs_path))
import pdb
pdb.run('import Leap')


class ContextAwareListener(Leap.Listener):

    def __init__(self, controller):
        if controller is None:
            raise ValueError("Controller was not properly intialized...")

        super().__init__()
        self.controller = controller

    def __enter__(self):
        self.controller.add_listener(self)
        return self

    def __exit__(self):
        self.controller.remove_listener(self)

    def on_connect(self,controller):
        print("Connected..\n\n")

    def on_frame(self,controller):
        print("Frame available\n")
        frame = controller.frame()
        previous = controller.frame(1)

        #do something with the hand position inside the frame
        hand_props = hand_properties(frame)

        # with open('movement.txt', 'a+') as file:
        #     file.write(hand_props)
        return frame


def hand_properties(frame):
    hand = frame.hands.rightmost

    position = hand.palm_position #(x,y,z) in millimeters
    velocity = hand.palm_velocity
    normal_vector = hand.palm_normal

    pitch = hand.direction.pitch# x axis angle
    yaw = hand.direction.yaw# y axis
    roll = hand.palm_normal.roll#z axis relative to normal_vector
    return position, pitch, yaw, roll


def follow_hand(handID=0, frame=None):
    hand = frame.hand(handID)
    return

def is_previous_frame(curr_frame,prev_id):
    if curr_frame.id == prev_id:
        return True
    return False

def main():

    # listener = ContextAwareListener()
    controller = Leap.Controller()
    #
    # while not controller.is_connected():
    #     #wait here doing whatever
    #     print("...")
    #print("Controller Connected...\n\n")
    with ContextAwareListener(controller) as listener:
    # controller.add_listener(listener)

        # Keep this process running until Enter is pressed
        print("Press Enter to quit...")
        current_line = sys.stdin.readline().strip()
        print(current_line)
        #while current_line  is None:
        while True:

            frame = listener.on_frame(listener.controller)
            print(hand_properties(frame))
            try:

                current_line = sys.stdin.readline()
            except KeyboardInterrupt:
                print("Terminating Leap Motion Connection...")

    # finally:
    #     controller.remove_listener(listener)

if __name__ == "__main__":
    main()
