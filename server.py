#!/usr/bin/python

import socket
import os
from threading import Thread

# initialize the song-to-votes dictionary
songdict = dict()

can_vote = dict()

connections = []

sock = socket.socket()
host = "192.168.43.104"
port = 12373

sock.bind((host, port))
sock.listen(5)

print "now listening!"


# find the highest voted song
def get_best_song():
    max_votes = -1
    best_song = ""
    print songdict
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

    for thread_id in can_vote:
        can_vote[thread_id] = True

    for connection in connections:
        connection.send("Enter your vote for the next song.\n")


# checks for user input, updates vote count based on song the user voted for
def check_for_input(connection, thread_id):
    can_vote[thread_id] = True
    while True:
        vote = connection.recv(4096)
        print vote
        if vote.isdigit() and int(vote) <= len(songdict.keys()) and can_vote[thread_id]:
            songdict[int(vote)][1] = songdict[int(vote)][1] + 1
            print songdict
            can_vote[thread_id] = False
        print "now get the vote"


def handle_initial_connection():
    thread_id = 0
    while True:
        connection, addr = sock.accept()
        print 'Got connection from', addr
        initial_message = "Thank you for connecting to this pi\n"
        initial_message += "Please vote for a song\n"
        counter = 1
        for song in os.listdir("songs"):
            initial_message += str(counter) + " " + song + "\n"
            counter += 1
        connection.send(initial_message)

        connections.append(connection)

        thread = Thread(target=check_for_input, args=(connection, thread_id,))
        thread.start()
        thread_id += 1

initialize_votes()

# create thread to handle new connections
thread = Thread(target=handle_initial_connection)
thread.start()

while True:
    best_song, max_votes = get_best_song()
    initialize_votes()
    os.system("omxplayer songs/" + best_song)

sock.close()
