## Test with m4.xlarge EC2 on AWS

The directories here contain the times obtained during the execution of the tests on 1-8 instances of m4.xlarge.

LoadTimeCache and LoadTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_load_time/0_3M/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory through the Spark REST API
* 6 result directories that contain the results obtained in 32*10 test for each ds_size (0_3M, 0_5M, 1M, 2M, 5M or 10M). So for the LoadTime with m4.xlarge 3840 tests were performed.


OverallTimeCache and OverallTimeNoCache contains:
* A bash script that moves specific logs (e.g. from a directory 2_worker_2_cores_overall_time/0_3M/) to the Spark log directory and executes the python script.
* A python script that allows to get the load_time of all the logs in the Spark log directory through the Spark REST API
* 24 result directories that contain the results obtained in 32*10 test for each ds_size (0_3M, 0_5M, 1M, 2M, 5M or 10M). So for the OverallTime with m4.xlarge 3840 tests were performed.


Images contains the plots obtained by using the python scripts:
- plot_overall_time.py: this script shows 4 functions with an X axis in [1-8] (so X cores).
- plot_overall_time2.py: this script shows 8 functions with an X axis in [1-4] (so X workers).
- plot_stacked_chart.py: this script shows the contribution of the different phases in the overall time by increasing the number of cores [1-4] given a number of Worker received as parameter.
- plot_stacked_chart2.py: this script shows the contribution of the different phases in the overall time by increasing the number of Spark Workers [1-8] given a number of cores per worker received as parameter.

## Usage of the python scripts


`$ python3 ./plot_overall_time.py Cache 10M overall` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/overall_time_10M_cache.png)


`$ python3 ./plot_overall_time.py NoCache 10M overall` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/overall_time_10M_no_cache.png)


`$ python3 ./plot_overall_time2.py Cache 10M overall` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_x_cores_f_worker/overall_time_10M_cache.png)


`$ python3 ./plot_overall_time2.py NoCache 10M overall` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_x_cores_f_worker/overall_time_10M_no_cache.png)


`$ python3 ./plot_stacked_chart.py 7 Cache 10M` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_contrib/contrib_7_worker_10M_cache.png)


`$ python3 ./plot_stacked_chart.py 7 NoCache 10M` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_contrib/contrib_7_worker_10M_no_cache.png)


`$ python3 ./plot_stacked_chart.py 3 Cache 10M` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_contrib2/contrib_y_workers_3_cores_cache.png)

`$ python3 ./plot_stacked_chart.py 3 NoCache 10M` 

![](https://github.com/StevenSalazarM/Apache-Spark-Scalability-Analysis/blob/master/test_m4_xlarge/Images/prova_contrib2/contrib_y_workers_3_cores_no_cache.png)

