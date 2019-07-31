#! /usr/bin/env python
import socket

#print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

def find_host_ip():
    hostname = socket.gethostname()
    IP = socket.getfqdn(hostname)
    return socket.gethostbyname(IP)

def find_client_ip(name_search=''):#we need to ask user for exact robot name
    #remote_hostname = 'robots name'
    client_ip = socket.gethostbyname(name_search)
    return client_ip

def create_client_settings(ssid='',user='', passw=''):
    
    client_ip = find_client_ip(ssid)

    with open("client_settings.txt", "r") as file:
            
        file.write("IP:{}".format(client_ip))
        file.write("user:{}".format(user))
        file.write("password:{}".format(passw))
    return

def create_network_settings(ip_address='', front_port='',back_port=''):#could be abstracted to work with a  dict

    with open("network_settings.txt","r") as file:
        file.write("IP:{}".format(ip_address))
        file.write("frontend:{}".format(front_port))
        file.write("backend:{}".format(back_port))
    return
if __name__ == "__main__":
    print(find_host_ip())