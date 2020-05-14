import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys

# can be Cache or NoCache
cache = sys.argv[1]
# can be 0_3M, 0_5M, 1M, 2M, 5M or 10M
ds_size = sys.argv[2]
# can be overall, shuffle, jobs, out or load
time_type = sys.argv[3]

dir_type="OverallTime"		
if time_type == "load":
	dir_type="LoadTime"
# each list in average_overall_time contain the values related to workers and cores (e.g. the first list is the used for 1 cores and worker. The last one is for 4 cores 8 worker)
average_overall_time = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
workers = [1, 2, 3, 4, 5, 6, 7, 8]
for c in range(4):
	for w in range(8):
		file_ov = open(dir_type+cache+"/results_"+time_type+"_"+ds_size+"/"+str(w+1)+"_worker_"+str(c+1)+"_cores_"+time_type+"_time.txt", "r") 
		count=0		
		# lets get the average value of X test in each file
		# count is used to calculate X		
		for line in file_ov:
			if line == "\n": break 
			count += 1    		
			average_overall_time[c][w] += float(line)
		average_overall_time[c][w] /= count
		file_ov.close()

fig = plt.figure(figsize=(18,6))
ax = fig.add_subplot(111)
ax.plot(workers, average_overall_time[0], label='1 Core ['+cache+']', color='red')
ax.plot(workers, average_overall_time[1], label='2 Cores ['+cache+']', color='y')
ax.plot(workers, average_overall_time[2], label='3 Cores ['+cache+']', color='orange')
ax.plot(workers, average_overall_time[3], label='4 Cores ['+cache+']', color='grey')

# imo it is better to have legend on center left than on top right inside the plot
leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.add_artist(leg1)

ax.set_title("Overall Time "+cache+" ("+ds_size+" dataset)")
plt.xlabel('Number of workers')
plt.ylabel('Seconds')
plt.show()
