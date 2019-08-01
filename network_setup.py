#! /usr/bin/env python
import socket
import nmap

#print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

def find_ip_by_ssid(ssid=''):
    if ssid.strip() is None:
        raise Exception("Sorry SSID cannot be empty")
    port_scanner = nmap.PortScanner()
    base_ip = str(find_host_ip().split('.')[0:2])#truncate the last portion so we just have the family it belongs to
    possible_ips = [base_ip + '.' + str(num) for num in range (1,255)]#generate from 1-254 since the first and last are localhost and broadcast
    for ip in possible_ips:
        port_scanner.scan(ip, '22-9090')
        for host in port_scanner.all_hosts():
            if port_scanner[host].hostname() == ssid:
                return host
    
    print('@ERROR: SSID not found!\n\n')
    return None


def find_host_ip():
    hostname = socket.gethostname()
    IP = socket.getfqdn(hostname)
    return socket.gethostbyname(IP)

def find_client_ip(name_search=''):#we need to ask user for exact robot name
    #remote_hostname = 'robots name'
    client_ip =''
    try:
        ip = socket.getfqdn(name_search.strip())
        print(ip)
        # client_ip = socket.gethostbyname(ip)
        client_ip = socket.gethostbyname(name_search.strip())
        print(client_ip)
    except Exception as e:
        print("Could not find robot on network, make sure the name provided is correct and that robot is on the same network...")
        print(e)
        print()
    return client_ip

def create_client_settings(ssid='',user='', passw=''):
    
    client_ip = find_client_ip(ssid)

    with open("client_settings.txt", "w") as file:
        file.write("IP:{}\n".format(client_ip))
        file.write("user:{}\n".format(user))
        file.write("password:{}\n".format(passw))
    return

def create_network_settings(ip_address='', front_port='',back_port=''):#could be abstracted to work with a  dict

    try:
        with open("network_settings.txt","w") as file:
            file.write("IP:{}\n".format(ip_address))
            file.write("frontend:{}\n".format(front_port))
            file.write("backend:{}\n".format(back_port))
    except IOError as e:
        print(e)

    return

def input_loop(ssid='',user='',passw=''):
    inputs = {}#robot name, user, password

    if len(user.strip()) > 0:
        inputs['user'] = user

    if len(ssid.strip()) > 0:
        inputs['ssid'] = ssid

    if len(passw.strip()) > 0:
        inputs['passw'] = passw

    while len(inputs)  != 3:
        try:
            if  'ssid' not in inputs.keys():
                #next arg
                ssid = input("Robot SSID(no whitespaces please):").strip()
                inputs['ssid'] = ssid

            if  'user' not in inputs.keys():
                #next arg
                user = input("Robot login username(no whitespaces please):").strip()
                inputs['user'] = user

            if  'passw' not in inputs.keys():
                passw = input("Robot login password(no whitespaces please):").strip()
                inputs['passw'] = passw

        except Exception as e:
            print(e)
            
    return inputs

def main(user='',passw=''):
    
    #do something for the input
    try:
        ins = input_loop(user=user.strip(), passw=passw.strip())#dict with ssid,user and password
        create_client_settings(ssid=ins['ssid'],user=ins['user'], passw=ins['passw'])
        create_network_settings(ip_address=find_host_ip(), front_port=4200, back_port=8000)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # main()
    find_ip_by_ssid(ssid='Niryo')#Not tested yet