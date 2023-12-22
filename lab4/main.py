
import boto3
import time


# Initialization of AWS service clients
ec2 = boto3.client('ec2', region_name='ap-south-1')
autoscale = boto3.client('autoscaling', region_name='ap-south-1')
cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')

# Configuration Variables
AMI_ID = ''
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'EC2 Tutorial'
SECURITY_GROUPS = ['launch-wizard-1']
INSTANCE_PROFILE_NAME = ''  # This is the name of the IAM instance profile

# Reading user data script (your startup script)
with open('startup4.sh', 'r') as file:
    user_data_script = file.read()

# Define Launch Configuration
autoscale.create_launch_configuration(
    LaunchConfigurationName='MyWebLaunchConfig5',
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    SecurityGroups=SECURITY_GROUPS,
    UserData=user_data_script,
    KeyName=KEY_NAME,
    IamInstanceProfile=INSTANCE_PROFILE_NAME  # Using the IAM instance profile name here
)

# Define AutoScaling Group
autoscale.create_auto_scaling_group(
    AutoScalingGroupName='MyWebASG5',
    LaunchConfigurationName='MyWebLaunchConfig5',
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    AvailabilityZones=['ap-south-1a']
)

# Scale up policy
scale_up_policy = autoscale.put_scaling_policy(
    AutoScalingGroupName='MyWebASG5',
    PolicyName='ScaleUp',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=1,
    Cooldown=60
)

# Scale down policy
scale_down_policy = autoscale.put_scaling_policy(
    AutoScalingGroupName='MyWebASG5',
    PolicyName='ScaleDown',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=-1,
    Cooldown=60
)

# Create CloudWatch Alarms for scaling policies
# Scale up
cloudwatch.put_metric_alarm(
    AlarmName='ScaleUpAlarm',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    Threshold=70,
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=2,
    AlarmActions=[scale_up_policy['PolicyARN']]
)

# Scale down
cloudwatch.put_metric_alarm(
    AlarmName='ScaleDownAlarm',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    Threshold=30,
    ComparisonOperator='LessThanThreshold',
    EvaluationPeriods=2,
    AlarmActions=[scale_down_policy['PolicyARN']]
)

print("AutoScaling setup complete!")

# Waiting for instances to launch
print("Waiting for instances to launch...")
time.sleep(180)

# Get instance information for those in the AutoScaling group
response = autoscale.describe_auto_scaling_groups(
    AutoScalingGroupNames=['MyWebASG5']
)

instance_ids = [instance['InstanceId'] for instance in response['AutoScalingGroups'][0]['Instances']]

# Fetch the public DNS of these instances
ec2_descriptions = ec2.describe_instances(InstanceIds=instance_ids)
for reservation in ec2_descriptions['Reservations']:
    for instance in reservation['Instances']:
        print(f"Public DNS for instance {instance['InstanceId']}: {instance['PublicDnsName']}")