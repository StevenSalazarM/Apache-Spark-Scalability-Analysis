#!/bin/bash

if [[ $1 == "" || $2 == "" || $3 == "" ]]; then
	echo "First param is max number of Workers."
	echo "Second param is max number of Cores."
	echo "Thirst param is the size of the dataset [0_3M, 0_5M, 1M, 2M, 5M or 10M]."
else
	for (( cw=1; cw<=$1; cw++ ))
	do
		for (( cc=1; cc<=$2; cc++ ))
		do
			cp ./${cw}_worker_${cc}_cores_load_time/$3/* ~/logs/
			sleep 10 # sleep is needed because Spark recognizes new files only after 10 seconds due to its refreshing system with 10s period
			python3 ./get_times.py ~/logs/ $cw $cc $3
			rm ~/logs/*
		done
	done
fi	
