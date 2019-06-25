#!/usr/bin/env python

#https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73

import paramiko

class SSH_Session:

    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return

    def __enter__(self,data_send=[]):
        self.__init__()

        return

    def __exit__(self):
        self.client.close()
        self.client = None
        return



ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='',username='',password='')

#downloading a file from remote

ftp_client = ssh_client.open_sftp()
ftp_client.client('remote-file','local-path')
ftp_client.close()

#uploading a file local to remote

ftp_client = ssh_client.open_sftp()
ftp_client.put('local-path','remote-path')
ftp_client.close()
