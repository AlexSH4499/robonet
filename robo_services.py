#!/bin/env/python

import os, sys
from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty

from samples import leap_motion_controller
import network_setup

#taken from
#https://www.sharats.me/posts/the-ever-useful-and-neat-subprocess-module/
io_queue = Queue()

def stream_watcher(identifier, stream):

    for line in stream:
        io_queue.put((identifier, line))
    
    if not stream.closed:
        stream.close()

    return

proc = Popen('command_here', stdout=PIPE, stderr=PIPE)


Thread(target=stream_watcher, name='stdout-watcher',
        args=('STDOUT', proc.stdout)).start()
Thread(target=stream_watcher, name='stderr-watcher',
        args=('STDERR', proc.stderr)).start()

def printer():

    while True:

        try:

            item = io_queue.get(True, 1)
        
        except Empty:

            if proc.poll() is not None:
                break
        
        else:

            identifier, line = item
            print(identifier + ':' + line)

printer_thread = Thread(target=printer, name='printer').start()

def initialize():
    client_settings = network_setup.load_client_settings()
    net_settings = network_setup.load_network_settings()
    client_ip =  client_settings['IP']
    user = client_settings['user']
    passw = client_settings['password']
    #TODO: Possible problem here due to robot needing backend up first
    #optimally we might want to use subprocesses or create other terminals
    command = ""
    os.system(f"start /wait cmd /c ssh {user}@{client_ip}")#this is the sample way to open a new cmd
    # os.system(f"ssh {user}@{client_ip}")
    # os.system(f"{passw}")

    server_ip = net_settings['IP']
    server_port = net_settings['backend']
    #setup the backend
    os.system("dir;pause")
    os.system(f"cd RESTAPI")
    os.system(f"python manage.py {server_ip}:{server_port}")

    #this should be run in Python 2.7
    # leap_motion_controller.main(ip=net_settings['IP'], port=net_settings['backend'], api='requests',
    #                             user='mec123', passw='mec123')
    return


if __name__ == "__main__":
    initialize()