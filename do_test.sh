#!/bin/bash

# this script allows to launch X test in an automatic way by executing './do_test.sh ds_size exe_cores class_name'
if [[ ( $1 == "" || $2 == "" || $3 == "") ]]; then
        echo "First param is used for file size: original, 1gb, 5gb, 10gb, 15gb."
        echo "Second param is used for executor cores [2,8]."
        echo "Third param is used for class name: LoadCache, LoadNoCache, CarAccidentsCache or CarAccidentsNoCache."
else
        for (( c=1; c<=10; c++ ))
                        do
			# the binary jar file is assumed to be on ~/Documents/apache-spark-car-accidents/bin/
			# the jar file takes 3 params: the master location, the directory containing NY car accidents dataset and test_number
			# the dataset is  assumed to be on ~/Documents/apache-spark-car-accidents/files/ds_size/
			# $c is the test number that is being performed (used to save the results in directory with $c name)
			# the result message obtained by spark-submit is saved into ~/test_logs
                        spark-submit --executor-cores $2 --class it.polimi.middleware.spark.car.accidents.$3 ~/Documents/apache-spark-car-accidents/bin/car_accidents.jar spark://172.31.2.81:7077 ~/Documents/apache-spark-car-accidents/files/$1/ $c > ~/test_logs && echo "OK $c"
                        done

fi
