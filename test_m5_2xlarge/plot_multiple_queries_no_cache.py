import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

path = "~/logs/"
average_overall_time = [0,0,0,0,0,0,0,0,0]
average_read_time = [0,0,0,0,0,0,0,0,0]
average_stage0_time = [0,0,0,0,0,0,0,0,0]
queries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for q in range(9):
		file_ovnc = open("MultipleQueriesNoCache/results_overall/"+str(q+1)+"_overall_time.txt", "r") 
		file_readnc = open("MultipleQueriesNoCache/results_read/"+str(q+1)+"_read_time.txt", "r")
		file_stage0 = open("MultipleQueriesNoCache/results_stage0/"+str(q+1)+"_stage0_time.txt", "r")
				
		count=0
		for line in file_ovnc:
			if line == "\n": break 
			count += 1    			
			average_overall_time[q] += float(line)
		average_overall_time[q] /= count
		count=0

		for line in file_readnc:
			if line == "\n": break 
			count += 1    			
			average_read_time[q] += float(line)
		average_read_time[q] /= count
		count=0
		for line in file_stage0:
			if line == "\n": break 
			count += 1    			
			average_stage0_time[q] += float(line)
		average_stage0_time[q] /= count

		file_stage0.close()
		file_ovnc.close()
		file_readnc.close()

fig = plt.figure(figsize=(20,6))
fig.subplots_adjust(left=0.05,right=0.87)
ax = fig.add_subplot(111)
ax.plot(queries, average_overall_time, label='Overall T.[No Cache]', color='blue')
ax.plot(queries, average_read_time, label='Read T.[No Cache]', color='green')
ax.plot(queries, average_stage0_time, label='Stage 0 T.[No Cache]', color='violet')
leg1 = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.add_artist(leg1)
ax.set_title("Multiple Queries No Cache (15GB dataset and 3 worker with 8 cores)")
plt.xlabel('Number of Queries')
plt.ylabel('Seconds')
plt.show()
