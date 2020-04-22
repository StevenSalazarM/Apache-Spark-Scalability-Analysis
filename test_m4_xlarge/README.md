## Test with m4.xlarge VM on AWS

The directories here contain the different times obtained during the execution of the tests on 2-4 instances of m4.xlarge.

LoadTimeCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_load_time/15gb/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory
* 9 txt files that contains the load time obtained in 9 test types (e.g. 2_worker_2_cores_load_time.txt contains the loadtime obtained in 10 tests using 2 workers with 2 cores)

## Usage

