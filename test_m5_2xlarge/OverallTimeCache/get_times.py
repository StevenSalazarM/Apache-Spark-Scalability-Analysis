import sys
import os
import urllib.request
import json 
from datetime import datetime, timedelta

# this python script is used to get the load time in each test
if __name__ == "__main__":
	path = sys.argv[1]
	executors = int(sys.argv[2])
	cores = int(sys.argv[3])
	files = os.listdir(path)
	results_out = open("./results_output/"+str(executors)+"_worker_"+str(cores)+"_cores_output_time.txt", "a")
	results_jobs = open("./results_jobs/"+str(executors)+"_worker_"+str(cores)+"_cores_jobs_time.txt", "a")
	results_overall = open("./results_overall/"+str(executors)+"_worker_"+str(cores)+"_cores_overall_time.txt", "a")	
	results_shuffle = open("./results_shuffle/"+str(executors)+"_worker_"+str(cores)+"_cores_shuffle_time.txt", "a")
	# we want to calculate the times in each test, so we consider all files in path
	for f in files:
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/") as url:
  	  		data = json.loads(url.read().decode())
		r = json.dumps(data)
		loaded_r = json.loads(r)
		real_duration_time_in_sec = loaded_r['attempts'][0]['duration']/1000
		# print("Overall time is: "+str(real_duration_time_in_sec))
		FMT = '%H:%M:%S.%f'
		
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/jobs/") as jobs_data:
  	  		jobs_data = json.loads(jobs_data.read().decode())
		jobs_r = json.dumps(jobs_data)
		loaded_jobs = json.loads(jobs_r)
		# for the REST API the first query is the last job
		job0 = loaded_jobs[2]
		job1 = loaded_jobs[1]
		job2 = loaded_jobs[0]
		job0_duration = datetime.strptime(job0['completionTime'][11:-3], FMT) - datetime.strptime(job0['submissionTime'][11:-3], FMT)

		# time may be negative if we move from one day to other so we must add an extra day in this case
		if job0_duration.total_seconds() < 0:
			job0_duration += timedelta(days=1)

		job1_duration = datetime.strptime(job1['completionTime'][11:-3], FMT) - datetime.strptime(job1['submissionTime'][11:-3], FMT)

		# time may be negative if we move from one day to other so we must add an extra day in this case		
		if job1_duration.total_seconds() < 0:
			job1_duration += timedelta(days=1)

		job2_duration = datetime.strptime(job2['completionTime'][11:-3], FMT) - datetime.strptime(job2['submissionTime'][11:-3], FMT)

		# time may be negative if we move from one day to other so we must add an extra day in this case		
		if job2_duration.total_seconds() < 0:
			job2_duration += timedelta(days=1)
		
		jobs_duration=job0_duration.total_seconds()+job1_duration.total_seconds()+job2_duration.total_seconds()
		print(f+"Jobs duration: "+str(jobs_duration)+" from " +str(job0_duration.total_seconds())+" " +str(job1_duration.total_seconds())+ "  " + str(job2_duration.total_seconds()))		
		output_duration = 0
		total_shuffle_time=0
		for s in range(6):
			with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/stages/"+str(s)+"/0/") as stage_time:
  	  			stage_data = json.loads(stage_time.read().decode())
			stage_r = json.dumps(stage_data)
			loaded_stage = json.loads(stage_r)
			stage_tasks = int(loaded_stage['numTasks']) / (executors*cores)
			with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/stages/"+str(s)+"/0/taskSummary?quantiles=0.5") as shuffle_time:
				shuffle_data = json.loads(shuffle_time.read().decode())
			shuffle_r = json.dumps(shuffle_data)
			loaded_shuffle = json.loads(shuffle_r)
			
			if s%2 == 0:
				# writeTime is the time spent in writing to blocks (through the WebUI or the REST API there is not way to find the read time on local blocks)
				# however it is approximate to 0 since reading in local memory is really fast.
				shuffle_write_time = (loaded_shuffle['shuffleWriteMetrics']['writeTime'][0] * stage_tasks)/1000000000
				total_shuffle_time += shuffle_write_time
			else:
				# fetchWaitTime is the time spent reading remote shuffle blocks, it is expressed in milliseconds
				# fetchWaitTime is often 0, so if reading for remote blocks is near to 0 reading local blocks is still 0 and prob thats why it is not shown in the WebUI
				shuffle_read_time = (loaded_shuffle['shuffleReadMetrics']['fetchWaitTime'][0] * stage_tasks)/1000				
				total_shuffle_time += shuffle_read_time
				# output is related only to odd stages
				out_stage_start_time = loaded_stage['submissionTime'][11:-3]
				out_stage_end_time = loaded_stage['completionTime'][11:-3]
				output_duration += (datetime.strptime(out_stage_end_time, FMT) - datetime.strptime(out_stage_start_time, FMT)).total_seconds() - shuffle_read_time
				
		# print("output stage: "+str(output_duration))
		# print("Total shuffle contribution is: "+str(total_shuffle_time))		
		results_out.write(str(output_duration)+"\n")
		results_shuffle.write(str(total_shuffle_time)+"\n")
		results_jobs.write(str(jobs_duration)+"\n")
		results_overall.write(str(real_duration_time_in_sec)+"\n")
	results_out.close()
	results_shuffle.close()
	results_jobs.close()
	results_overall.close()

