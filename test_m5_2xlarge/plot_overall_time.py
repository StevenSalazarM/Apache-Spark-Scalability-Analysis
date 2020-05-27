import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


average_overall_time = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
cores = [1, 2, 3, 4, 5, 6, 7, 8]
for w in range(3):
	for c in range(8):
		file_ov = open("OverallTimeCache/results_overall/"+str(w+1)+"_worker_"+str(c+1)+"_cores_overall_time.txt", "r") 
		count=0
		for line in file_ov:
			if line == "\n": break 
			count += 1    			
			average_overall_time[w][c] += float(line)
		average_overall_time[w][c] /= count
		file_ov.close()

fig = plt.figure(figsize=(18,6))
fig.subplots_adjust(left=0.05,right=0.87)
ax = fig.add_subplot(111)
ax.plot(cores, average_overall_time[0], label='1 Worker [Cache]', color='red')
ax.plot(cores, average_overall_time[1], label='2 Workers [Cache]', color='y')
ax.plot(cores, average_overall_time[2], label='3 Workers [Cache]', color='orange')


average_overall_time = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
for w in range(3):
	for c in range(8):
		file_ov = open("OverallTimeNoCache/results_overall/"+str(w+1)+"_worker_"+str(c+1)+"_cores_overall_time.txt", "r") 
		count=0
		for line in file_ov:
			if line == "\n": break 
			count += 1    			
			average_overall_time[w][c] += float(line)
		average_overall_time[w][c] /= count
		file_ov.close()

ax.plot(cores, average_overall_time[0], label='1 Worker [NoCache]', color='blue')
ax.plot(cores, average_overall_time[1], label='2 Workers [NoCache]', color='green')
ax.plot(cores, average_overall_time[2], label='3 Workers [NoCache]', color='violet')

#ax.plot(cores, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='4 cores', color='yellow')
#ax.plot(cores, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='5 cores', color='black')
#ax.plot(cores, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='6 cores', color='orange')
#ax.plot(cores, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='7 cores', color='grey')
#ax.plot(wo, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='8 cores', color='violet')
# Add first legend:  only labeled data is included

leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Add second legend for the maxes and mins.
# Manually add the first legend back
ax.add_artist(leg1)
ax.set_title("Overall Time Cache and No Cache (15GB dataset)")
plt.xlabel('Number of cores')
plt.ylabel('Seconds')
plt.show()
