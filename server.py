#!/usr/bin/python

import socket
import os

# globals

# initialize the song-to-votes dictionary
songdict = dict()
connections = []

sock = socket.socket()
host = "192.168.43.104"
port = 12345

sock.bind((host, port))
sock.listen(5)


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


def handle_initial_connection():
    connection, addr = sock.accept()
    print 'Got connection from', addr
    initial_message = "Thank you for connecting to this pi\n"
    initial_message += "Please vote for a song\n"
    initial_message += "1. example.mp3"
    connection.send(initial_message)
    connections.append(connection)
initialize_votes()
while True:
    handle_initial_connection()

    for connection in connections:
        vote = connection.recv(4096)
        print vote
        if vote.isdigit():
            print "valid vote"
        if vote == "quit":
            break

for connection in connections:
    connection.close()
