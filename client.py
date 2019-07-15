import socket


sock = socket.socket()

MSG_LEN = 1024#WE decide this parameter
port = 80
ip_address = ''
sock.connect((ip_address, port))

sock.recv(MSG_LEN)

sock.close()

def main():
    #create a socket

    sock = socket.socket()
    sock.connect((ip_address, port))

    #while some condition, receive data and process
    while True:
        sock.recv(MSG_LEN)

    #finished
    sock.close()


if __name__ == "__main__":

    main()