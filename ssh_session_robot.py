#https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73

import paramiko


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
