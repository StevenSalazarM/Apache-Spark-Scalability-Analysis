import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
from matplotlib.ticker import MaxNLocator

# can be Cache or NoCache
cache = sys.argv[1]
# can be 0_3M, 0_5M, 1M, 2M, 5M or 10M
ds_size = sys.argv[2]
# can be overall, shuffle, jobs, output (if you want load just add an if inside the for c in range(4) cos load is in another directory)
time_type = sys.argv[3]

# each list in average_overall_time contain the values related to the four cores of each VM
average_overall_time = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cores = [1, 2, 3, 4]

for w in range(8):
	for c in range(4):
		file_ov = open("OverallTime"+cache+"/results_"+time_type+"_"+ds_size+"/"+str(w+1)+"_worker_"+str(c+1)+"_cores_"+time_type+"_time.txt", "r") 
		count=0
		# lets get the average value of X test in each file
		# count is used to calculate X
		for line in file_ov:
			if line == "\n": break 
			count += 1    			
			average_overall_time[w][c] += float(line)
		average_overall_time[w][c] /= count
		file_ov.close()

fig = plt.figure(figsize=(18,6))
ax = fig.add_subplot(111)
ax.plot(cores, average_overall_time[0], label='1 Worker ['+cache+']', color='red')
ax.plot(cores, average_overall_time[1], label='2 Workers ['+cache+']', color='y')
ax.plot(cores, average_overall_time[2], label='3 Workers ['+cache+']', color='orange')
ax.plot(cores, average_overall_time[3], label='4 Workers ['+cache+']', color='blue')
ax.plot(cores, average_overall_time[4], label='5 Workers ['+cache+']', color='black')
ax.plot(cores, average_overall_time[5], label='6 Workers ['+cache+']', color='grey')
ax.plot(cores, average_overall_time[6], label='7 Workers ['+cache+']', color='violet')
ax.plot(cores, average_overall_time[7], label='8 Workers ['+cache+']', color='green')

# imo it is better to have legend on center left than on top right inside the plot
leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.add_artist(leg1)

# Since we have only 4 values for X axis, by default X.5 is added so imo it is better to consider only integer values
ticker = fig.gca()
ticker.xaxis.set_major_locator(MaxNLocator(integer=True))

ax.set_title("Overall Time "+cache+" ("+ds_size+" dataset)")
plt.xlabel('Number of cores')
plt.ylabel('Seconds')
plt.show()
