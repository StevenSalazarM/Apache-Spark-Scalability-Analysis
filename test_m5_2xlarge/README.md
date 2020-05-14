## Test with m5.2xlarge EC2 on AWS

The directories here contain the times obtained during the execution of the tests on 1-4 instances of m5.2xlarge.

LoadTimeCache and LoadTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_load_time/15gb/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory through the Spark REST API
* 1 result directory that contain the results obtained in 24*10 test for each ds_size (for now only 15gb was performed). So for the LoadTime with m5.2xlarge 480 tests were performed.


OverallTimeCache and OverallTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_overall_time/15gb/) to the Spark log directory and executes the python script.
* A python script that allows to get the overall_time of all the logs in the Spark log directory through the Spark REST API
* 4 result directory that contain the results obtained in 24*10 test for each ds_size (for now only 15gb was performed). So for the OverallTime with m5.2xlarge 480 tests were performed.


MultipleQueriesCache and MultipleQueriesNoCache contains:
* A bash script that moves specific logs (from a directory 1, 2, 3, 4, 5, 6, 7, 8 or 9 since the tests with multiple queries start from 1 Query to 9 Queries) to the Spark log directory and executes the python script.
* A python script that allows to get the overall_time of all the logs in the Spark log directory through the Spark REST API.
* 4 result directory that contain the results obtained in 9*10 test for each ds_size (for now only 15gb was performed). So for MultipleQueries with m5.2xlarge 180 tests were performed.

Images contains the plots obtained by using the python scripts:
- plot_multiple_queries_cache.py
- plot_multiple_queries_no_cache.py
- plot_multiple_queries.py
- plot_overall_time_cache.py
- plot_overall_time_no_cache.py
- plot_overall_time.py
- plot_stacked_chart.py

## Usage of the python scripts

`$ python3 ./plot_multiple_queries_cache.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/multiple_queries_cache.png)


`$ python3 ./plot_multiple_queries_no_cache.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/multiple_queries_no_cache.png)


`$ python3 ./plot_multiple_queries.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/multiple_queries_vs.png)


`$ python3 ./plot_overall_time_cache.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/overall_time_cache.png)


`$ python3 ./plot_overall_time_no_cache.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/overall_time_no_cache.png)


`$ python3 ./plot_overall_time.py` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/overall_time_vs.png)


`$ python3 ./plot_stacked_chart.py 3 Cache` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/contrib_3_worker_cache.png)


`$ python3 ./plot_stacked_chart.py 3 NoCache` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m5_2xlarge/Images/contrib_3_worker_no_cache.png)


