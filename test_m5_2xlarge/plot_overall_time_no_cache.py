import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


path = sys.argv[1]
executors = int(sys.argv[2])
cores = int(sys.argv[3])
average_overall_time = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
workers = [1, 2, 3]
for w in range(3):
	for c in range(8):
		file_ov = open("OverallTimeCache/results_overall/"+str(w+1)+"_worker_"+str(c+1)+"_cores_overall_time.txt", "r") 
		count=0
		for line in file_ov:
			if line == "\n": break 
			count += 1    			
			average_overall_time[w][c] += int(line)
		average_overall_time[w][c] /= count
		file_ov.close()

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.plot(workers, average_overall_time[0], label='1 Worker', color='red')
ax.plot(workers, average_overall_time[1], , label='2 Workers', color='green')
ax.plot(workers, average_overall_time[2], label='3 Workers', color='blue')
#ax.plot(workers, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='4 cores', color='yellow')
#ax.plot(workers, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='5 cores', color='black')
#ax.plot(workers, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='6 cores', color='orange')
#ax.plot(workers, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='7 cores', color='grey')
#ax.plot(wo, [0, 279, 280, 299, 300, 306, 312, 322, 340], label='8 cores', color='violet')
# Add first legend:  only labeled data is included

leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Add second legend for the maxes and mins.
# Manually add the first legend back
ax.add_artist(leg1)

plt.show()
