import boto3
import time
import os

# Replace these with your own credentials
aws_profile = ''
aws_access_key = ''
aws_secret_key = ''
region_name = 'ap-south-1'


def read_startup_script(script_path):
    with open(script_path, 'r') as file:
        return file.read()


startup_script = read_startup_script('script.sh')

os.environ['AWS_PROFILE'] = aws_profile

# Initialize Boto3 clients
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key,
                          region_name=region_name)

def launch_instance1(instance_type, image_id):
    response = ec2_client.run_instances(
        InstanceType=instance_type,
        IamInstanceProfile={
            'Arn': 'arn:aws:iam::075736006885:instance-profile/demorole'
        },
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        KeyName='EC2 Tutorial',  # Replace with your key pair name
        SecurityGroupIds=['launch-wizard-1'],  # Replace with your security group ID
        UserData= startup_script )
    instance_ide = response['Instances'][0]['InstanceId']
    return instance_ide




def launch_instance(instance_type, image_id):
    response = ec2_client.run_instances(
        InstanceType=instance_type,
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        IamInstanceProfile={
            'Arn': 'arn:aws:iam::075736006885:instance-profile/demorole'
        },
        KeyName='EC2 Tutorial',  # Replace with your key pair name
        SecurityGroupIds=['launch-wizard-1'],  # Replace with your security group ID
        UserData= '''#!/bin/bash
echo "Hello from the User Data script!" > /tmp/userdata.txt
''' )
    instance_ide = response['Instances'][0]['InstanceId']
    return instance_ide


def list_running_instances():
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = []
    for reservation in response['Reservations']:
        instances.extend(reservation['Instances'])
    return instances


def check_instance_health(instance_id):
    response = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    if response['InstanceStatuses']:
        instance_status = response['InstanceStatuses'][0]['InstanceStatus']['Status']
        # system_status = response['InstanceStatuses'][0]['SystemStatus']['Status']
        return instance_status
    else:
        return "Not Found", "Not Found"




def stop_instances(instance_ids):
    ec2_client.stop_instances(InstanceIds=instance_ids)


def terminate_instances(instance_ids):
    ec2_client.terminate_instances(InstanceIds=instance_ids)


if __name__ == "__main__":
    t2_micro_ami = "ami-0da59f1af71ea4ad2"  # Replace with the actual Amazon Linux AMI ID

    instance_type = "t2.micro"

    # Launch instances
    instance_ids = []
    id = launch_instance1(instance_type=instance_type, image_id= t2_micro_ami)
    instance_ids.append(id)
    for _ in range(2):
        instance_id = launch_instance(instance_type, t2_micro_ami)
        instance_ids.append(instance_id)

    print("Launched instances:", instance_ids)

    time.sleep(30)  # Allow instances to initialize
    for instance_id in instance_ids:
        instance_health = check_instance_health(instance_id)
        print(f"Instance {instance_id} - Instance Health: {instance_health}")

    # List running instances
    running_instances = list_running_instances()
    print("Running instances:", [instance['InstanceId'] for instance in running_instances])

    instance_id = instance_ids[0]

# Wait for the instance to be running
    # print("Waiting for the instance to start...")
    while True:
        instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance_state = instance_info['Reservations'][0]['Instances'][0]['State']['Name']
        if instance_state == 'running':
            public_dns = instance_info['Reservations'][0]['Instances'][0]['PublicDnsName']
            ipv4_address = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
            break
        time.sleep(5)

        # Open the instance's public DNS in a browser to verify the static website
    print(f"Open this URL in your browser: http://{public_dns}/")
    print("OR")
    print(f"Open this URL in your browser: http://{ipv4_address}/")    

    input("Please press enter to start the process to stop the insatnces")
    # Stop instances
    stop_instances(instance_ids)
    print("Stopping instances...")

    # Wait for instances to stop
    waiter = ec2_client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=instance_ids)
    print("Instances stopped.")

    # Terminate instances
    terminate_instances(instance_ids)
    print("Terminating instances...")
