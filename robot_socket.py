import socket
from socket import SOCK_STREAM,AF_INET

MSGLEN = 1024# in bytes
class RobotSocket:

    def __init__(self, socket=None):

        if socket is None:
            #AF_INET is referencing IPv4 family
            #Sockstream TCP protocol
            self.sock = socket.socket(socket.AF_INET, SOCK_STREAM)

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

    def __receive(self):
        chunks=[]
        bytes_received = 0

        while bytes_received < MSGLEN:

            chunk = self.sock.recv(min(MSGLEN - bytes_received,2048))
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
    
    def _bind(self, ip_port_combo=(,)):
        self.sock.bind(ip_port_combo)
        self.sock.listen(5)#listening mode for 5 connections
        return 

    def _listen(self, sock=None):
        while True:

            conn, address = s.accept()
            print('Connection from:{}'.format(address))

            #send a confirmation message of achieved connection
            conn.send('Connection Established!')

            conn.close()