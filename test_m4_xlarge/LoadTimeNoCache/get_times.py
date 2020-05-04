import sys
import os
import urllib.request
import json 
from datetime import datetime

# this python script is used to get the load time in each test
if __name__ == "__main__":
	path = sys.argv[1]
	executors = sys.argv[2]
	cores = sys.argv[3]
	ds_size = sys.argv[4]
	files = os.listdir(path)
	output = open("./results_load_"+ds_size"+/executors+"_worker_"+cores+"_cores_load_time.txt", "a")	
	# we want to calculate the load time in each test, so we consider all files in path
	for f in files:
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/stages/0/0/") as url:
  	  		data = json.loads(url.read().decode())
		r = json.dumps(data)
		loaded_r = json.loads(r)
		# the duration that is shown in the WebUI is not available in the Rest API (it is obtained by performing completion_time - submitted_time) but honestly I prefer to calculate it myself by checking the time required for each executor
		# so we sum the time spent by each executor
		# sum_exe_time = 0		
		# for e in range(int(executors)):
		#	sum_exe_time += loaded_r['executorSummary']['1']['taskTime']
		# the time obtained is in milliseconds so it should be divided by 1000 and then by 60 to be shown in minutes	
		# also it should be divided by executors*cores since we considered the sum of all and we didnt consider before that each executor paralellize its own workload based on the number of cores	
		# avg_exe_time_in_min = (sum_exe_time/(int(executors)*int(cores)))/60000

		FMT = '%H:%M:%S.%f'
		# duration = completionTime - submissionTime (considering only Hours:Minutes:Seconds)
		duration = datetime.strptime(loaded_r['completionTime'][11:-3], FMT) - datetime.strptime(loaded_r['submissionTime'][11:-3], FMT)
		duration_in_nano = duration.total_seconds()*1000000000
		# num_tasks is the number of tasks normalized, for example if we had in total 120 tasks with 2 cores and 2 exectors
		# we had a parallelization of 4 tasks and we should multiply the shuffle_write_time by 30 like if they were executed in serial way.
		# If this wasnt clear you can check the web UI event timeline and see that only around 30 tasks contribute to the duration time
		num_tasks = int(loaded_r['numCompleteTasks'])/(int(cores)*int(executors))
		# now we should find out the shuffle write time
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/stages/0/0/taskSummary?quantiles=0.5") as shuffle_url:
  	  		shuffle_data = json.loads(shuffle_url.read().decode())
		shuffle_r = json.dumps(shuffle_data)
		loaded_shuffle = json.loads(shuffle_r)
		# the shuffle write time should be considered to be present in each tasks 
		total_shuffle_write_time = loaded_shuffle['shuffleWriteMetrics']['writeTime'][0] * num_tasks
		real_duration_time_in_sec = (duration_in_nano - total_shuffle_write_time)/1000000000
		# print("avergare write time: "+str(loaded_shuffle['shuffleWriteMetrics']['writeTime'][0]))
		# print("Shuffle Write Time: "+str(total_shuffle_write_time)) 
		# print("Old time is: "+str(duration.total_seconds()))
		# print("Real time is: "+str(real_duration_time_in_sec))
		output.write(str(real_duration_time_in_sec)+"\n")
	output.close()

