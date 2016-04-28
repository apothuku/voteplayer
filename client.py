import socket

sock = socket.socket()
host = "192.168.43.104"
port = 12365

sock.connect((host, port))
print sock.recv(4096)

while True:
    user_input = raw_input()
    sock.send(user_input)
    sock.recv(4096)

sock.close()
