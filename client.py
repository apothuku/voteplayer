import socket

sock = socket.socket()
host = "192.168.43.104"
port = 12345

sock.connect((host, port))
print sock.recv(4096)

while True:
    user_input = str(input("Enter your vote"))
    sock.send(user_input)

sock.close()
