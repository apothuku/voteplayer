#!/usr/bin/python

import socket
import os

# initialize the song-to-votes dictionary
songdict = dict()

# find the highest voted song
def get_best_song():
	max = 0
	best_song = None
	for song in songdict:
		curr = songdict[song]
		if curr > max:
			max = curr
			best_song = song
	return best_song
# initialize number of votes for each song to 0
def initialize_votes():
	for song in os.listdir("songs"):
    songdict.update({song: 0})

# create the server
s = socket.socket()
host = "192.168.43.104"
port = 12345
s.bind((host, port))

initialize_votes()

s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection from', addr
	initial_message = "Thank you for connecting to this pi\n"
	initial_message += "Please vote for a song\n"
	initial_message += "1. example.mp3"
	c.send(initial_message)
	c.close()
