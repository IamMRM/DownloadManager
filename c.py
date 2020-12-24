from socket import *
import sys

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientIP =  '192.168.1.7'
clientPort = 12000
buf=1024

file_name = raw_input("Enter Filename: ")
clientSocket.sendto(file_name,(clientIP,clientPort))
f=open("roshan.txt","w+")
print "hello1"
data,server = clientSocket.recvfrom(buf)
try:
    while(data):
        f.write(data)
        clientSocket.settimeout(2)
        data,server = clientSocket.recvfrom(buf)
except timeout:
    f.close()
    clientSocket.close()
    print "File Downloaded"
