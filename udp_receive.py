import sys
import socket

address = ('', 50007)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(address)

while True:
	data,addr = s.recvfrom(1024)
	try:
		sys.stdout.write(data.decode('utf-8'))
	except:
		print (" ")


s.close()


