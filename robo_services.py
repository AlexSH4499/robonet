#!/bin/env/python

import os, sys

from samples import leap_motion_controller
import network_setup

def initialize():
    client_settings = network_setup.load_client_settings()
    net_settings = network_setup.load_network_settings()
    client_ip =  client_settings['IP']
    user = client_settings['user']
    passw = client_settings['password']
    #TODO: Possible problem here due to robot needing backend up first
    #optimally we might want to use subprocesses or create other terminals
    command = ""
    os.system(f"start /wait cmd /c {command}")#this is the sample way to open a new cmd
    os.system(f"ssh {user}@{client_ip}")
    os.system(f"{passw}")

    server_ip = net_settings['IP']
    server_port = net_settings['backend']
    #setup the backend
    os.system(f"cd RESTAPI")
    os.system(f"python manage.py {server_ip}:{server_port}")

    #this should be run in Python 2.7
    # leap_motion_controller.main(ip=net_settings['IP'], port=net_settings['backend'], api='requests',
    #                             user=client_settings['user'], passw=client_settings['password'])
    return


if __name__ == "__main__":
    initialize()