

ROBOT_IP_ADDRESS = '192.168.1.27'#OR 36
USER= 'niryo'
PASS = 'robotics'

# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

# based on code provided by raymond mosteller (thanks!)

import base64
import getpass
import os
import socket
import sys
import traceback

import paramiko
from paramiko.py3compat import input


REMOTE_LIBRARY_DIR = "/home/niryo/catkin_ws/devel/"
NIRYO_API_SCRIPT = "niryo_one_example_python_api.py"
# setup logging
paramiko.util.log_to_file("demo_sftp.log")

# Paramiko client configuration
UseGSSAPI = True  # enable GSS-API / SSPI authentication
DoGSSAPIKeyExchange = True
Port = 22

def auth_credentials():
    # get hostname
    username = ""
    if len(sys.argv) > 1:
        hostname = sys.argv[1]
        if hostname.find("@") >= 0:
            username, hostname = hostname.split("@")
    else:
        hostname = input("Hostname: ")
    if len(hostname) == 0:
        print("*** Hostname required.")
        sys.exit(1)

    if hostname.find(":") >= 0:
        hostname, portstr = hostname.split(":")
        Port = int(portstr)


    # get username
    if username == "":
        default_username = getpass.getuser()
        username = input("Username [%s]: " % default_username)
        if len(username) == 0:
            username = default_username
    if not UseGSSAPI:
        password = getpass.getpass("Password for %s@%s: " % (username, hostname))
    else:
        password = None

    return username, password


def host_key_and_type(hostkeytype=None, hostkey=None):
    try:
        host_keys = paramiko.util.load_host_keys(
            os.path.expanduser("~/.ssh/known_hosts")
        )
    except IOError:
        try:
            # try ~/ssh/ too, because windows can't have a folder named ~/.ssh/
            host_keys = paramiko.util.load_host_keys(
                os.path.expanduser("~/ssh/known_hosts")
            )
        except IOError:
            print("*** Unable to open host keys file")
            host_keys = {}
    hostname=ROBOT_IP_ADDRESS
    if hostname in host_keys:
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]
        print("Using host key of type %s" % hostkeytype)

    return hostkeytype, hostkey


def send_file(hostname=ROBOT_IP_ADDRESS, hostkey=None, username=USER, password=PASS, file_to_send=NIRYO_API_SCRIPT, directory=REMOTE_LIBRARY_DIR):
    t = paramiko.Transport((hostname, Port))
    t.connect(hostkey, username,   password,)
    sftp = paramiko.SFTPClient.from_transport(t)

    # dirlist on remote host
    # dirlist = sftp.listdir(directory)
    # print("Dirlist: %s" % dirlist)
    # BETTER: use the get() and put() methods
    print(sftp.put(localpath=file_to_send,remotepath=directory+file_to_send, confirm=True ))#remote directory must include file to be sent in the path
    # sftp.get("demo_sftp_folder/README", "README_demo_sftp")

    t.close()

    return


def connect():
    # now, connect and use paramiko Transport to negotiate SSH2 across the connection
    try:
        send_file(hostname=ROBOT_IP_ADDRESS, hostkey=None, username=USER,password=PASS,
                 file_to_send=NIRYO_API_SCRIPT,directory=REMOTE_LIBRARY_DIR)
    except Exception as e:
        print("*** Caught exception: %s: %s" % (e.__class__, e))
        traceback.print_exc()
        sys.exit(1)

    return


if __name__ == '__main__':
    connect()
