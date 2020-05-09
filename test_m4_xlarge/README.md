## Test with m4.xlarge EC2 on AWS

The directories here contain the different times obtained during the execution of the tests on 1-4 instances of m4.xlarge.

LoadTimeCache and LoadTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_load_time/0_3M/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory through the Spark REST API
* 6 result directories that contain the results obtained in 32*10 test for each ds_size (0_3M, 0_5M, 1M, 2M, 5M or 10M). So in total those 6 directories contain 1920 tests.

## Usage

