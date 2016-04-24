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
    max_votes = -1
    best_song = ""
    for key, value in songdict.iteritems():
        curr_votes = value[1]
        if curr_votes > max_votes:
            max_votes = curr_votes
            best_song = value[0]
    print best_song + " " + str(max_votes)
    return (best_song, max_votes)


# initialize number of votes for each song to 0
def initialize_votes():
    counter = 0
    for song in os.listdir("songs"):
        songdict[counter] = [song, 0]
        counter += 1


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
            songdict[vote][1] = songdict[vote][1] + 1
        if vote == "quit":
            break
    # if song is not playing, play the most popular song
    if not os.system("sh currently_playing.sh"):
        best_song, max_votes = get_best_song()
        os.system("omxplayer " + best_song)
        initialize_votes()

for connection in connections:
    connection.close()
