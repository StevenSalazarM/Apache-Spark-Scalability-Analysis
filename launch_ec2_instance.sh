#!/bin/bash

if [[ ( $1 == "" || $2 == "") ]]; then
        echo "First param is the template name."
        echo "Second param is the number of instances."
else
        # it takes as param $1 launchtemplate name and $2 for the number of instances
	# before executing this script make sure that you have an AMI of the VM that you would like to clone and also create a template from the Web Console specifying the placement group and the instance type 
        aws ec2 run-instances   --image-id ami_id --key-name key_name --subnet-id subnet_id --launch-template LaunchTemplateName=$1 --count $2 && echo "$2 Instances with name $1 have been launched, check the web console if you want to verify the completion of this script."
fi

