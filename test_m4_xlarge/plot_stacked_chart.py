import matplotlib.pyplot as plt
import sys

# worker can be 1, 2 or 3
worker = sys.argv[1]
# cache can be Cache or NoCache
cache = sys.argv[2]
# ds_size can be 0_3m, 0_5M, 1M, 2M, 5M, 10M. M means millions of rows
ds_size = sys.argv[3]

test_type=["1 core","2 cores","3 cores", "4 cores"]

load_time = [0] * 4
overall_time = [0] * 4
shuffle_time = [0] * 4
output_time = [0] * 4
computing_time = [0] * 4
jobs_time = [0] * 4

# lets fill the previous arrays for each Y core
for c in range(4):
	
	# average overall_time between tests present in results_overall_time directory
	file_ov = open("OverallTime"+cache+"/results_overall_"+ds_size+"/"+worker+"_worker_"+str(c+1)+"_cores_overall_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		overall_time[c] += float(line)
		count += 1    			
	overall_time[c] /= count
	file_ov.close()

	# average jobs_time between tests present in results_jobs_time directory
	file_ov = open("OverallTime"+cache+"/results_jobs_"+ds_size+"/"+worker+"_worker_"+str(c+1)+"_cores_jobs_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		jobs_time[c] += float(line)
		count += 1    			
	jobs_time[c] /= count
	file_ov.close()

	# average load_time between tests present in results_load_time directory
	file_ov = open("LoadTime"+cache+"/results_load_"+ds_size+"/"+worker+"_worker_"+str(c+1)+"_cores_load_time.txt", "r") 
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
	file_ov = open("OverallTime"+cache+"/results_shuffle_"+ds_size+"/"+worker+"_worker_"+str(c+1)+"_cores_shuffle_time.txt", "r") 
	count=0
	for line in file_ov:
		if line == "\n": break 
		shuffle_time[c] += float(line)
		count += 1    			
	shuffle_time[c] /= count
	file_ov.close()

	# average output_time between tests present in results_output_time directory
	file_ov = open("OverallTime"+cache+"/results_output_"+ds_size+"/"+worker+"_worker_"+str(c+1)+"_cores_output_time.txt", "r")	
	count=0
	for line in file_ov:
		if line == "\n": break 
		output_time[c] += float(line)
		count += 1    			
	output_time[c] /= count
	file_ov.close()

# print(load_time)
# print(overall_time)
# print(jobs_time)
# print(shuffle_time)
# print(output_time)


# computing time is obtained as jobs_time-load_time-shuffle_time-output_time
# Spark delay is obtained as overall_time - jobs_time
# jobs_time is obtained as sum(job1,job2,job3) or in other words sum(query1, query2, query3)

computing_time=[j-l-s-out for j, l, s, out in zip(jobs_time, load_time, shuffle_time, output_time)]
print(computing_time)
spark_delay = [ov-jobs for ov, jobs in zip(overall_time, jobs_time)]
fig = plt.figure(figsize=(18,6))
ax = fig.add_subplot(111)


bar_load = ax.barh(test_type, load_time, color="green",label="Load Time")  

bar_computing = ax.barh(test_type, computing_time, left=load_time, color="brown", label="Computing Time")

# we want shuffle bar to be on left of bar_computing so we must consider left=load+computing
load_and_computing = [x + y for x, y in zip(load_time, computing_time)]
bar_shuffle = ax.barh(test_type, shuffle_time, left=load_and_computing, color="y", label="Shuffle Time")

# we want out bar to be on left of bar_shuffle so we must consider left=load+computing+shuffle
load_and_computing_and_shuffle = [x + y for x, y in zip(load_and_computing, shuffle_time)]
bar_out = ax.barh(test_type, output_time, left=load_and_computing_and_shuffle,color="b",label="Output Time")

# we want spark bar to be on left of bar_out so we must consider left=load+computing+shuffle+out
delay_introduced_margin = [x + y for x, y in zip(load_and_computing_and_shuffle, output_time)]
bar_spark = ax.barh(test_type, spark_delay, left=delay_introduced_margin,color="gray",label="Spark delay Time")


# Add counts above the bar graphs
for rect in bar_load + bar_computing+bar_out+bar_spark:
    height = rect.get_height()
    width  = rect.get_width()
    bl = rect.get_xy()
    x = 0.5*rect.get_width() + bl[0]
    y = 0.5*rect.get_height() + bl[1]
    ax.text(x, y,'%.1f' % float(width),ha='center',va='center', color='w')

# imo it is better to have legend on center left than on top right inside the plot
leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.add_artist(leg1)

ax.set_title("Contribution of different phases in the overall time with "+ds_size+" rows dataset and "+cache)
plt.xlabel('Seconds')
plt.ylabel(worker+' Worker - Y Cores')
plt.show()
