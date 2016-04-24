#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "need to specify file"
	exit 0
fi

scp $1 pi@192.168.43.104:proj/
