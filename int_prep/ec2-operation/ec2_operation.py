import subprocess
import time
import os

REGION = "us-east-2"

with open("ec2.log") as f:
    for line in f:
        instance_id = line.strip()

        if not instance_id:
            continue

        command_stop = ["aws", "ec2", "stop-instances", "--instance-ids", instance_id, "--region", REGION ]
        command_modify = ["aws", "ec2", "modify-instance-attribute", "--instance-id", instance_id, "--region", REGION, "--instance-type", '{"Value":"m7g.4xlarge"}']
        command_desc = ["aws", "ec2", "describe-instances", "--instance-ids", instance_id, "--region", REGION,"--query", "Reservations[].Instances[].{ID:InstanceId,State:State.Name}"]
        command_start = ["aws", "ec2", "start-instances", "--instance-ids", instance_id, "--region", REGION ]

        
        # # time.sleep(1)
        # subprocess.run(command_2)
        # time.sleep(1)
        # # os.system("clear")
        # os.system("echo running describe instance")
        
        # subprocess.run(command_stop)
        # subprocess.run(command_modify)
        subprocess.run(command_desc)
        # subprocess.run(command_start)
        time.sleep(1)
        

# aws ec2 describe-instances --instance-ids i-0e8cd368c0606fb41 --region eu-west-3  --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name}'
#aws ec2 stop-instances --instance-ids i-0e8cd368c0606fb41 --region eu-west-3
#aws ec2 describe-instances --instance-ids i-0e8cd368c0606fb41 --region eu-west-3
