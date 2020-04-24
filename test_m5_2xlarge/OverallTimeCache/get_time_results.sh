#!/bin/bash

if [[ $1 == "" || $2 == "" ]]; then
	echo "First param is max number of Workers."
	echo "Second param is max number of Cores."
else
	for (( cw=1; cw<=$1; cw++ ))
	do
		for (( cc=1; cc<=$2; cc++ ))
		do
			cp ./${cw}_worker_${cc}_cores_overall_time/15gb/* ~/logs/
			sleep 10 # sleep is needed because Spark recognizes new files only after 10 seconds due to its refreshing system with 10s period
			python3 ./get_times.py ~/logs/ $cw $cc
			rm ~/logs/*
		done
	done
fi	
