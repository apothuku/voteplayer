#!/usr/bin/python

import socket
import os
from threading import Thread

# initialize the song-to-votes dictionary
songdict = dict()

sock = socket.socket()
host = "192.168.43.104"
port = 12363

sock.bind((host, port))
sock.listen(5)

print "now listening!"


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
    counter = 1
    for song in os.listdir("songs"):
        songdict[counter] = [song, 0]
        counter += 1


# checks for user input, updates vote count based on song the user voted for
def check_for_input(connection):
    while True:
        vote = connection.recv(4096)
        print vote
        if vote.isdigit() and int(vote) <= len(songdict.keys()):
            songdict[int(vote)][1] = songdict[int(vote)][1] + 1


def handle_initial_connection():
    while True:
        connection, addr = sock.accept()
        print 'Got connection from', addr
        initial_message = "Thank you for connecting to this pi\n"
        initial_message += "Please vote for a song\n"
        counter = 1
        for song in os.listdir("songs"):
            initial_message += str(counter) + " " + song
            counter += 1
        connection.send(initial_message)

        thread = Thread(target=check_for_input, args=(connection,))
        thread.start()

initialize_votes()

# create thread to handle new connections
thread = Thread(target=handle_initial_connection)
thread.start()

while True:
    best_song, max_votes = get_best_song()
    initialize_votes()
    os.system("omxplayer songs/" + best_song)

sock.close()
