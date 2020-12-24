# -*- coding: utf-8 -*-
from socket import *
serverPort = 12004
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("10.7.48.88",serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
    connectionSocket, addr = serverSocket.accept()
    print "Request Accepted from Some Client ..."
    file = open("audio.mp4", "rb")
    data = file.read(1024)
    while(data):
    	connectionSocket.send(data)
    	data = file.read(1024) 
    connectionSocket.close()
    print "Client Served Successfully !"
    x = raw_input("Press 0 to close server or 1 to continue")
    if( x == "0"):
    	break
