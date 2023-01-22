#!/bin/bash

echo $1

if [ $1 == 5 ] 
then
	python3 src/joke_MGR.py
	exit
fi

echo "starting all console output is now under JJ control"

python3 src/main.py $1
