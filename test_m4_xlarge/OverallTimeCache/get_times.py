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
	files = os.listdir(path)
	# output = open("./"+executors+"_worker_"+cores+"_cores_load_time.txt", "a")	
	# we want to calculate the load time in each test, so we consider all files in path
	for f in files:
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/") as url:
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
		end_time = loaded_r['attempts'][0]['endTime'][11:-3]
		start_time = loaded_r['attempts'][0]['startTime'][11:-3]
		
		duration = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
		duration_in_nano = duration.total_seconds()*1000000000
		# num_tasks is the number of tasks normalized, for example if we had in total 120 tasks with 2 cores and 2 exectors
		# we had a parallelization of 4 tasks and we should multiply the shuffle_write_time by 30 like if they were executed in serial way.
		# If this wasnt clear you can check the web UI event timeline and see that only around 30 tasks contribute to the duration time
		# num_tasks = int(loaded_r['numCompleteTasks'])/(int(cores)*int(executors))
		# now we should find out the shuffle write time
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/jobs/") as jobs_data:
  	  		jobs_data = json.loads(jobs_data.read().decode())
		jobs_r = json.dumps(jobs_data)
		loaded_jobs = json.loads(jobs_r)
		job0 = loaded_jobs[2]
		job1 = loaded_jobs[1]
		job2 = loaded_jobs[0]
		job0_duration = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
		# the shuffle write time should be considered to be present in each tasks 
		# total_shuffle_write_time = loaded_shuffle['shuffleWriteMetrics']['writeTime'][0] * num_tasks
		# real_duration_time_in_sec = (duration_in_nano - total_shuffle_write_time)/1000000000
		real_duration_time_in_sec = loaded_r['attempts'][0]['duration']/1000
		
		# print("avergare write time: "+str(loaded_shuffle['shuffleWriteMetrics']['writeTime'][0]))
		# print("Shuffle Write Time: "+str(total_shuffle_write_time)) 
		# print("Old time is: "+str(duration.total_seconds()))
		print("Real time is: "+str(real_duration_time_in_sec))
		print("Diff of End-Start: "+str(duration.total_seconds())) 		
		# output.write(str(real_duration_time_in_sec)+"\n")
	# output.close()

