import sys
import os
import urllib.request
import json 
from datetime import datetime

# this python script is used to get the load time in each test
if __name__ == "__main__":
	path = sys.argv[1]
	query = sys.argv[2]
	files = os.listdir(path)
	results_read = open("./results_read/"+query+"_read_time.txt", "a")
	results_overall = open("./results_overall/"+query+"_overall_time.txt", "a")
	results_stage_0 = open("./results_stage0/"+query+"_stage0_time.txt", "a")	
	# we want to calculate the times in each test, so we consider all files in path
	for f in files:
		with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/") as url:
  	  		data = json.loads(url.read().decode())
		r = json.dumps(data)
		loaded_r = json.loads(r)
		real_duration_time_in_sec = loaded_r['attempts'][0]['duration']/1000
		# print("Overall time is: "+str(real_duration_time_in_sec))
		FMT = '%H:%M:%S.%f'
		read_duration = 0
		total_shuffle_time=0
		for s in range(2*int(query)):
			with urllib.request.urlopen("http://localhost:18080/api/v1/applications/"+f+"/stages/"+str(s)+"/0/") as stage_time:
  	  			stage_data = json.loads(stage_time.read().decode())
			stage_r = json.dumps(stage_data)
			loaded_stage = json.loads(stage_r)		
			if s%2 == 0:
				read_stage_start_time = loaded_stage['submissionTime'][11:-3]
				read_stage_end_time = loaded_stage['completionTime'][11:-3]
				if s == 0:
					read_duration_s_0 = (datetime.strptime(read_stage_end_time, FMT) - datetime.strptime(read_stage_start_time, FMT)).total_seconds()
				read_duration += (datetime.strptime(read_stage_end_time, FMT) - datetime.strptime(read_stage_start_time, FMT)).total_seconds()
				
				
		# print("output stage: "+str(output_duration))
		# print("Total shuffle contribution is: "+str(total_shuffle_time))		
		results_stage_0.write(str(read_duration_s_0)+"\n")
		results_read.write(str(read_duration)+"\n")
		results_overall.write(str(real_duration_time_in_sec)+"\n")
	results_stage_0.close()
	results_read.close()
	results_overall.close()

