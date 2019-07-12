#!/usr/bin/env python
import sys,os,inspect
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

DEFAULT_SEARCH_DIR = "\home\"

def find_sdk(directory):

    return

def add_sdk_to_path(sdk_dir):

    return

def ask_directory_to_search(search_dir=DEFAULT_SEARCH_DIR):

    return

def detect_system_running():

    return