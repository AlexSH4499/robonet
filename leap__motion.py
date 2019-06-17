import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

def hand_properties(frame):
    hand = frame.hands.rightmost

    position = hand.palm_position #(x,y,z) in millimeters
    velocity = hand.palm_velocity
    normal_vector = hand.palm_normal

    pitch = hand.direction.pitch# x axis angle
    yaw = hand.direction.yaw# y axis
    roll = hand.palm_normal.roll#z axis relative to normal_vector
    return position, pitch, yaw, roll


def follow_hand(handID=0, frame):
    hand = frame.hand(handID)
    pass

def is_previous(curr_frame,prev_id):
    if curr_frame.id == prev_id:
        return True
    return False

def main():

    # listener = ContextAwareListener()
    controller = Leap.Controller()

    while not controller.is_connected():
        #wait here doing whatever
        print("...")
    #print("Controller Connected...\n\n")
    with ContextAwareListener(controller) as listener:
    # controller.add_listener(listener)

        # Keep this process running until Enter is pressed
        print("Press Enter to quit...")
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            pass

    # finally:
    #     controller.remove_listener(listener)

if __name__ == "__main__":
    main()

class ContextAwareListener(Leap.Listener):

    def __init__(self, controller=None):
        self.super().controller = controller

    def __enter__(self):
        self.controller.add_listener(listener)


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

        with open('movement.txt', 'a+') as file:
            file.write(hand_props)
        return
