import matplotlib.pyplot as plt
import sys

# worker can be 1, 2 or 3
worker = sys.argv[1]
# cache can be Cache or NoCache
cache = sys.argv[2]

test_type=["1 core","2 cores","3 cores", "4 cores", "5 cores", "6 cores", "7 cores", "8 cores"]

load_time = [0] * 8
overall_time = [0] * 8
shuffle_time = [0] * 8
output_time = [0] * 8
computing_time = [0] * 8
jobs_time = [0] * 8

# lets fill the previous arrays for each Y core
for c in range(8):
	
	# average overall_time between tests present in results_overall_time directory
	file_ov = open("OverallTime"+cache+"/results_overall/"+worker+"_worker_"+str(c+1)+"_cores_overall_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		overall_time[c] += float(line)
		count += 1    			
	overall_time[c] /= count
	file_ov.close()

	# average jobs_time between tests present in results_jobs_time directory
	file_ov = open("OverallTime"+cache+"/results_jobs/"+worker+"_worker_"+str(c+1)+"_cores_jobs_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		jobs_time[c] += float(line)
		count += 1    			
	jobs_time[c] /= count
	file_ov.close()

	# average load_time between tests present in results_load_time directory
	file_ov = open("LoadTime"+cache+"/results_load/"+worker+"_worker_"+str(c+1)+"_cores_load_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 			
		load_time[c] += float(line)		
		count += 1    			
	load_time[c] /= count
	# if the loadTime is related to NoCache then it should be multiplied by 3 since we considered a load_time of only one job
	if(cache=="NoCache"):
		load_time[c] *= 3
	file_ov.close()

	# average shuffle between tests present in results_shuffle_time directory
	file_ov = open("OverallTime"+cache+"/results_shuffle/"+worker+"_worker_"+str(c+1)+"_cores_shuffle_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		shuffle_time[c] += float(line)
		count += 1    			
	shuffle_time[c] /= count
	file_ov.close()

	# average output_time between tests present in results_output_time directory
	file_ov = open("OverallTime"+cache+"/results_output/"+worker+"_worker_"+str(c+1)+"_cores_output_time.txt", "r")	
	count=0
	for line in file_ov:
		if line == "\n": break 
		output_time[c] += float(line)
		count += 1    			
	output_time[c] /= count
	file_ov.close()

# print(load_time)
print(overall_time)
print(jobs_time)
# print(shuffle_time)
# print(output_time)


# computing time is obtained as jobs_time-load_time-shuffle_time-output_time
# Spark delay is obtained as overall_time - jobs_time
# jobs_time is obtained as sum(job1,job2,job3) or in other words sum(query1, query2, query3)

computing_time=[j-l-s-out for j, l, s, out in zip(jobs_time, load_time, shuffle_time, output_time)]
spark_delay = [ov-jobs for ov, jobs in zip(overall_time, jobs_time)]
print(computing_time)
fig = plt.figure(figsize=(20,6))
fig.subplots_adjust(left=0.05,right=0.87)
ax = fig.add_subplot(111)


bar_load = ax.barh(test_type, load_time, color="green",label="Load Time")  

bar_computing = ax.barh(test_type, computing_time, left=load_time, color="brown", label="Computing Time")

load_and_computing = [x + y for x, y in zip(load_time, computing_time)]
bar_shuffle = ax.barh(test_type, shuffle_time, left=load_and_computing, color="y", label="Shuffle Time")

load_and_computing_and_shuffle = [x + y for x, y in zip(load_and_computing, shuffle_time)]
bar_out = ax.barh(test_type, output_time, left=load_and_computing_and_shuffle,color="b",label="Output Time")

delay_introduced_margin = [x + y for x, y in zip(load_and_computing_and_shuffle, output_time)]
bar_spark = ax.barh(test_type, spark_delay, left=delay_introduced_margin,color="gray",label="Spark delay Time")

# font = {'size'   : 5}


# Add counts above the two bar graphs
for rect in bar_load + bar_computing+bar_spark:
    height = rect.get_height()
    width  = rect.get_width()
    #plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    bl = rect.get_xy()
    x = 0.5*rect.get_width() + bl[0]
    y = 0.5*rect.get_height() + bl[1]
    ax.text(x, y,'%.1f' % float(width),ha='center',va='center', color='w')


leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.add_artist(leg1)
ax.set_title("Contribution of different phases in the overall time with 15GB dataset and "+cache)
plt.xlabel('Seconds')
plt.ylabel(worker+' Worker - Y Cores')
plt.show()
