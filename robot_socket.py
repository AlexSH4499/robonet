import socket, asyncio
from socket import SOCK_STREAM,AF_INET

MSGLEN = 1024# in bytes
'''

'''
class RobotSocket:

    def __init__(self, socket=None):

        if socket is None:
            #AF_INET is referencing IPv4 family
            #Sockstream TCP protocol
            # self.sock = socket.socket(socket.AF_INET, SOCK_STREAM)
            self.sock = socket.socket(socket.AF_INET, SOCK_DGRAM)#UDP
        else:
            self.sock = socket
        
    def connect(self,host, port):
        self.sock.connect((host, port))
    
    def __send(self, msg):
        total_sent = 0

        while total_sent < MSGLEN:
            sent = self.sock.send(msg[total_sent:])
            
            if sent == 0:
                raise RuntimeError("Socket connection has been broken")

            total_sent += sent

    async def __receive(self):
        chunks=[]
        bytes_received = 0

        while bytes_received < MSGLEN:

            chunk = await  self.sock.recv(min(MSGLEN - bytes_received,2048))
            if chunk == '':
                raise RuntimeError("Socket connection has been broken")

            chunks.append(chunk)
            bytes_received += len(chunk)
        return ''.join(chunks)

    def __enter__(self, ip_address='192.168.1.27', port=80):
        self.__init__()
        #self.sock.connect()
        self.connect((ip_address, port))
        return self

    def __exit__(self):

        self.sock.shutdown()
        self.sock.close()

        return
    
    def __bind(self, ip_port_combo=(,)):
        self.sock.bind(ip_port_combo)
        self.sock.listen(5)#listening mode for 5 connections
        return 

    def __listen(self, sock=None):
        while True:

            conn, address = self.sock.accept()
            print('Connection from:{}'.format(address))

            #send a confirmation message of achieved connection
            conn.send('Connection Established!')

            conn.close()

#UDP Server

ip_address = "127.0.0.1"
port = 20001
buffer_size = 1024

msg_from_server = "From Server"
bytes_to_send = str.encode(msg_from_server)

udp_server_socket = socket.socket(family=socket.AF_INET, type=DGRAM)

udp_server_socket.bind((ip_address, port))

print("UDP Server listening...")

while True:
    
    bytes_address_pair = udp_server_socket.recvfrom(buffer_size)
    message, address = bytes_address_pair
    # message, address = bytes_address_pair[0], bytes_address_pair[1]
    client_msg = "Client message:\n\t\t\t{}\n".format(message)
    client_ip = "Client IP Address: {}".format(address)

    print(client_msg)
    print(client_ip)

#UDP Client

msg_from_client = "Hello UDP Server..."
bytes_to_send = str.encode(msg_from_client)
server_address_port = ("127.0.0.1","20001")

buffer_size          = 1024

 

# Create a UDP socket at client side

udp_socket_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket


udp_socket_client.sendto(bytes_to_send , server_address_port)

 

msg_from_server = udp_socket_client.recvfrom(buffer_size)

 

msg = "Message from Server {}".format(msg_from_server[0])

print(msg)

async def main(server_address="192.168.1.27", server_port="20001"):
    msg_from_client =""
    bytes_to_send = str.encode(msg_from_client)
    # server_address, server_port = ("127.0.0.1","20001")
    buffer_size = 1024#(bits) need to determine this later

    #declare a socket

    with RobotSocket(ip_address=server_address, port=server_port) as udp_socket_client:

        #udp_socket_client.connect(server_address_port)
        response_from_server = await udp_socket_client.__receive()
        
        while  response_from_server != '\0':

            response_from_server = udp_socket_client.__receive()


if __name__ == "__main__":
    asyncio.run(main())