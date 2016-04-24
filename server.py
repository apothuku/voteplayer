#!/usr/bin/python

import socket

s = socket.socket()

host = "192.168.43.104"
port = 12345
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection from', addr
	initial_message = "Thank you for connecting to this pi\n"
	initial_message += "Please vote for a song\n"
	initial_message += "1. example.mp3"
	c.send(initial_message)
	c.close()

