import socket
from termios import tcflush, TCIFLUSH
import sys

sock = socket.socket()
host = "192.168.43.104"
port = 12375

sock.connect((host, port))
print sock.recv(4096)

while True:
    tcflush(sys.stdin, TCIFLUSH)
    user_input = raw_input()
    sock.send(user_input)
    print sock.recv(4096)

sock.close()
