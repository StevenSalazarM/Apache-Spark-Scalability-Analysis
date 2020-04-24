#!/bin/bash

for (( c=1; c<=9; c++ ))
	do
		cp ./${c}/* ~/logs/
		sleep 10 # sleep is needed because Spark recognizes new files only after 10 seconds due to its refreshing system with 10s period
		python3 ./get_times.py ~/logs/ $c
		rm ~/logs/*
	done

