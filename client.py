
import socket			

s = socket.socket()		
port = 12345				

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
print(s.recv(1024))
s.close()	
	
