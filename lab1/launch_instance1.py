import boto3
import time
import os

aws_profile = ''
aws_region = ''

# Read the startup script content from the file
def read_startup_script(script_path):
    with open(script_path, 'r') as file:
        return file.read()

# User data script to install Apache and copy website files
startup_script = read_startup_script('startup1.sh')

# Set AWS CLI profile using environment variable
os.environ['AWS_PROFILE'] = aws_profile
# Create an EC2 client
ec2_client = boto3.client('ec2',region_name=aws_region)


# Launch an instance
instance = ec2_client.run_instances(
    ImageId='ami-0da59f1af71ea4ad2',
    InstanceType='t2.micro',
    KeyName='EC2 Tutorial',
    IamInstanceProfile={
        'Arn': 'arn:aws:iam::075736006885:instance-profile/role'
    },
    SecurityGroupIds=['launch-wizard-1'],
    UserData=startup_script,
    MaxCount=1,
    MinCount=1
)

instance_id = instance['Instances'][0]['InstanceId']

# Wait for the instance to be running
print("Waiting for the instance to start...")
while True:
    instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_state = instance_info['Reservations'][0]['Instances'][0]['State']['Name']
    if instance_state == 'running':
        public_dns = instance_info['Reservations'][0]['Instances'][0]['PublicDnsName']
        ipv4_address = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
        break
    time.sleep(5)


print(f"Instance {instance_id} is running. Public DNS: {public_dns}")
print(f"Ipv4 Address: {ipv4_address}")

# Open the instance's public DNS in a browser to verify the static website
print(f"Open this URL in your browser: http://{public_dns}/")
print("OR")
print(f"Open this URL in your browser: http://{ipv4_address}/")