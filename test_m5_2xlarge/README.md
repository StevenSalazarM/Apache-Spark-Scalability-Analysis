## Test with m5.2xlarge EC2 on AWS

The directories here contain the different times obtained during the execution of the tests on 1-4 instances of m5.2xlarge.

LoadTimeCache and LoadTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_load_time/15gb/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory through the Spark REST API
* 1 result directory that contain the results obtained in 24*10 test for each ds_size (for now only 15gb was performed).

## Usage

