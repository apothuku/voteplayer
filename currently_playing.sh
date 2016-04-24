#!/bin/sh

#script that returns true if the SERVICE is being ran, false if otherwise

# the directory containing all songs
SONGPATH="/songs" 

# is this service currently being used?
SERVICE="omxplayer"

# check if the service is currently being used
ps ax | grep -v grep | grep $SERVICE > /dev/null