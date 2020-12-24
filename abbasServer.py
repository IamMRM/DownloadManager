from socket import *
import sys
import select
serverSocket= socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',12000))
bufferSize = 1024
print "The server is ready to receive"
data,addr = serverSocket.recvfrom(bufferSize)
print "Received File:",data.strip()
f = open(data.strip(),'r')

print "test File:"
data = f.read(bufferSize)
print "hello"
while(data):
    serverSocket.sendto(data,addr)
    print data
    data = f.read(bufferSize)
f.close()
print "Done the transfer"
serverSocket.close()
