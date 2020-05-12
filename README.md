# Apache-Spark-Performance-Analysis
The purpose of this project is to perform a scalability analysis in an application using the Apache-Spark Dataframe API.

## Tests
- The tests were performed using two EC2 Instances Types: m4.xlarge and m5.2xlarge. The directories test_m5_2xlarge and test_m4_xlarge contain the results obtained from 6 tests type (LoadTimeCache, LoadTimeNoCache, CarAccidentsCache, CarAccidensNoCache, CarAccidentsXQueriesCache and CarAccidentsXQueriesNoCache) and 7 different dataset (0.3M, 0.5M, 1M, 2M, 5M  and 10M rows of dataset and 15GB dataset size).
- do_test.sh is a bash script that was used to submit the spark application in an automated way, for example:

	`./do_test.sh 15gb 4 CarAccidentsCache`

	Submits CarAccidents 10 times passing as param 15gb dataset, 4 cores (per slave) and uses the Spark cache function.
	For the loading time another Spark Application was used, in order to obtain the time required to load the dataset just execute:

	`./do_test.sh 15gb 4 LoadTimeCache`


- small_fix.sh is a bash script that allows to execute some configuration commands from the Master to the Workers:

	`ssh ubuntu@worker_ip 'bash -s' < small_fix.sh`
	
	from the Master.	
- launch_ec2_instance.sh is a bash script that allows to launch a EC2 instance by passing as parameter *template_name* and *number_of_instances*: 
	
	`./launch_ec2_instance.sh worker_8_cores 3`

	**Before executing the script please read the comments inside *launch_ec2_instance.sh* **, you need to create the template from the AWS Web Console, then in the script set the values of subnet_id, key_name and ami_id that you prefer (be consistent with the values you selected during the template creation, subnet_id is any subnet_id since it is not possible to select both security_group and subnet in a template)

## Usage

### Requirements
- Apache-Spark 2.4.
- An account on AWS and the aws-cli. 
- Access to EC2 instances with at least 20GB memory (it depends on the type of test that you want to perform, for example if you want to use a 15GB dataset you should have at least 20GB)
- An Apache-Spark application, the results obtained in the two test directories are related to [Apache-Spark-Car-Accidents-in-NY](https://github.com/StevenSalazarM/Car-Accidents-in-NY/) application.

### Test replication


