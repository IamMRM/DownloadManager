import sys, getopt
from urlparse import urlparse
import socket

def main(argv):
	noConnections = ''
	timeInterval = ''
	typeConnection = ''
	webAddress= ''
	location = ''
	resume = ''
	try:
		if argv[0] == '-r':
			print 'You want to resume download'
		opts, args = getopt.getopt(argv[1:],"hn:i:c:f:o:",["nfile=","ifile=","cfile=","ffile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-n", "--nfile"):
			noConnections = arg
		elif opt in ("-i", "--ifile"):
			timeInterval = arg
		elif opt in ("-c", "--cfile"):
			typeConnection = arg
		elif opt in ("-f", "--ffile"):
			webAddress = arg
		elif opt in ("-o", "--ofile"):
			location = arg
	
	print 'output is "', noConnections,' ',timeInterval,' ',typeConnection, ' ',webAddress,' ',location
	########################
	o = urlparse(webAddress)
	webIP = o.netloc
	serverIP = socket.gethostbyname(webIP)
	print serverIP
	
if __name__ == "__main__":
	main(sys.argv[1:])
	