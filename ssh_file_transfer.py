import paramiko, base64

ROBOT_IP_ADDRESS = '192.168.1.36'
USER= ''
PASS = ''
def  start_client():

    key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
    client = paramiko.SSHClient()
    client.get_host_keys().add(ROBOT_IP_ADDRESS, 'ssh-rsa' , key)
    client.connect(ROBOT_IP_ADDRESS,username=USER, password=PASS)

    #Commands here
    stdin, stdout, stderr = client.exec_command('ls')

    for line in stdout:
        print('...' + line.strip('\n'))

    client.close()



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

    if hostname in host_keys:
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]
        print("Using host key of type %s" % hostkeytype)

    return hostkeytype, hostkey


def send_file(hostname=ROBOT_IP_ADDRESS, hostkey=None, username="niryo", password="robotics", file_to_send="demo_sftp.py", directory="demo_sftp_folder"):
    t = paramiko.Transport((hostname, Port))
    # t.connect(hostkey,  username,   password,gss_host=socket.getfqdn(hostname),
    #             gss_auth=UseGSSAPI, gss_kex=DoGSSAPIKeyExchange,)
    t.connect(hostkey, username,   password,)
    sftp = paramiko.SFTPClient.from_transport(t)

    # dirlist on remote host
    dirlist = sftp.listdir(directory)
    print("Dirlist: %s" % dirlist)

    # copy this demo onto the server
    # try:
    #     sftp.mkdir(directory)
    # except IOError:
    #     print("(assuming demo_sftp_folder/ already exists)")
    # with sftp.open("demo_sftp_folder/README", "w") as f:
    #     f.write("This was created by demo_sftp.py.\n")
    # with open(file_to_send, "r") as f:
    #     data = f.read()
    # sftp.open("demo_sftp_folder/demo_sftp.py", "w").write(data)
    # print("created demo_sftp_folder/ on the server")

    # # copy the README back here
    # with sftp.open("demo_sftp_folder/README", "r") as f:
    #     data = f.read()
    # with open("README_demo_sftp", "w") as f:
    #     f.write(data)
    # print("copied README back here")

    # BETTER: use the get() and put() methods
    print(sftp.put(localpath=file_to_send,remotepath=directory+file_to_send, confirm=True ))
    # sftp.get("demo_sftp_folder/README", "README_demo_sftp")

    t.close()

    return


def connect():
    # now, connect and use paramiko Transport to negotiate SSH2 across the connection
    try:
        # username, password = auth_credentials()
        # hostkeytype, hostkey = host_key_and_type()

        # t = paramiko.Transport((ROBOT_IP_ADDRESS, Port))
        # t.connect(
        #     None,
        #     "niryo",
        #     "robotics",
        #     # gss_host=socket.getfqdn(ROBOT_IP_ADDRESS),
        #     # gss_auth=UseGSSAPI,
        #     # gss_kex=DoGSSAPIKeyExchange,
        # )
        # sftp = paramiko.SFTPClient.from_transport(t)

        # # dirlist on remote host
        # dirlist = sftp.listdir(".")
        # print("Dirlist: %s" % dirlist)
        # copy this demo onto the server
        send_file(hostname=ROBOT_IP_ADDRESS, hostkey=None, username="niryo",password="robotics", file_to_send="niryo_one_example_python_api.py",directory="/home/niryo/catkin_ws/devel")
    except Exception as e:
        print("*** Caught exception: %s: %s" % (e.__class__, e))
        traceback.print_exc()
        # try:
        #    # t.close()
        # except:
        #     pass
        sys.exit(1)

    return


if __name__ == '__main__':

    connect()
