#!/usr/bin/python3

# based on https://docs.python.org/3/howto/sockets.html

# ----------------------------------------------------
#                       FTPClient
# ----------------------------------------------------
#
# Contains the main run loop of the script
#
#


import socket
import struct
import sys

# ---------------
#	Default		|
# ---------------

DEBUG = True
PORT = 21
FTP_HOST = "10.246.251.93"

class FTPClient:

    def __init__(self):
        self.DEBUG    = True
        self.PORT     = 21
        self.FTP_HOST = "10.246.251.93"

    def sendMessage(self, sock, str):
        # From Example
        # value = int(sys.argv[1])
        #
        # # pack and send our argument
        # data = struct.pack("i", value)
        # sock.send(data)

        data = struct.pack('s', str)
        sock.send(data)

    def receiveMessage(self, sock):
        # From Example
        # # get back a response and unpack it
        # receivedMessage = sock.recv(4)
        # chunk = struct.unpack("i", receivedMessage)
        # # take the first int only
        # message = chunk[0]

        receivedMessage = ''
        while True:
            receivedMessage = sock.recv(1024)
           
	    print("X" + receivedMessage) 
            if not receivedMessage:
                break

            if '220' in receivedMessage:
                if self.DEBUG:
                    print("DEBUG - " + receivedMessage)
                return receivedMessage
		break



    def getCommand(self,sock):
        """"This function is the user interface that parses a users desired command and value."""
        while True:
            user_input = raw_input("ftpclient>")
            user_token = user_input.split(" ")

            # value = int(sys.argv[1])

            # pack and send our argument
            data = struct.pack("s", user_input)
	    self.sendMessage(sock, user_input)

	    #Return message from server
	    self.receiveMessage(sock, user_input)

            command = user_token[0]
            value = user_token[1]

            if DEBUG:
            	print("Command:", command)
            	print("Value:", value)


def main():
    # if len(sys.argv) != 2 or not sys.argv[1].isdigit() :
    # 	print("Usage: " + str(sys.argv[0]) + " <int>")
    # 	exit(1)

    # create an INET, STREAMing socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # FTP Client
    ftp = FTPClient()
    # now connect to the web server on port 9223, which we've made our server listen to
    # change the hostname if not on the same server
    print("Connecting to FTP " + FTP_HOST + " at port " + str(PORT))
    sock.connect((FTP_HOST, PORT))

    # FTP is a 'server speaks first' system so recive a 220 banner
    ftp.receiveMessage(sock)


    # USER COMMAND
    ftp.sendMessage(sock, 'USER cs472\r\n')

    ftp.receiveMessage(sock)

    while True:
    	command = ftp.getCommand(sock)
	

    sock.close()


if __name__ == "__main__":
    main()
