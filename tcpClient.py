from socket import *
import time
import datetime

serverIP =  "10.7.48.88"
serverPort = 12004
clientSocket = socket(AF_INET, SOCK_STREAM)

sent_time = datetime.datetime.now()
print "Recieve Request sent to server at: "+str(sent_time)
sent_time = time.time()

clientSocket.connect((serverIP,serverPort))
file = open("audio.mp4","wb")
data = clientSocket.recv(1024)
while(data):
	file.write(data)
	data = clientSocket.recv(1024)

rcv_time = datetime.datetime.now()
print "Audio Successfully Copied from server at: "+str(rcv_time)
clientSocket.close()