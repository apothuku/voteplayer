import socket

s = socket.socket()
host = "192.168.43.104"
port = 12345

s.connect((host, port))
print s.recv(4096)

s.close()
