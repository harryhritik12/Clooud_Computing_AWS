import boto3

# def create_rds_instance(instance_name, db_username, db_password, security_group_id):
#     client = boto3.client('rds', region_name='ap-south-1')
#
#     response = client.create_db_instance(
#         DBName='FeedbackDB',
#         DBInstanceIdentifier=instance_name,
#         AllocatedStorage=20,
#         DBInstanceClass='db.t2.micro',
#         Engine='mysql',
#         MasterUsername=db_username,
#         MasterUserPassword=db_password,
#         VpcSecurityGroupIds=[
#             security_group_id,
#         ],
#         PubliclyAccessible=True,
#     )
#
#
#
#
#     print(f"RDS instance {instance_name} is being created. This might take some time.")
#     waiter = client.get_waiter('db_instance_available')
#     waiter.wait(DBInstanceIdentifier=instance_name)
#     print(f"RDS instance {instance_name} has been created!")
#
#
#
# # Replace these placeholders with actual values before running the script
# INSTANCE_NAME = "RDSInstanceMinshu"
# DB_USERNAME = "admins"
# DB_PASSWORD = "12345678"
# SECURITY_GROUP_ID = "sg-08fbb9d666995ffe7"
#
# create_rds_instance(INSTANCE_NAME, DB_USERNAME, DB_PASSWORD, SECURITY_GROUP_ID)

def read_startup_script(script_path):
    with open(script_path, 'r') as file:
        return file.read()

ec2_client = boto3.client('ec2')
startup_script = read_startup_script('startupscript.sh')

def launch_instance1(instance_type, image_id):
    response = ec2_client.run_instances(
        InstanceType=instance_type,
        IamInstanceProfile={
            'Arn': 'arn:aws:iam::075736006885:instance-profile/lab5'
        },
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        KeyName='rdsKEYpair',  # Replace with your key pair name
        SecurityGroupIds=['launch-wizard-1'],  # Replace with your security group ID
        UserData= startup_script )
    instance_ide = response['Instances'][0]['InstanceId']
    return instance_ide

t2_micro_ami = "ami-0da59f1af71ea4ad2"  # Replace with the actual Amazon Linux AMI ID

instance_type = "t2.micro"
id = launch_instance1(instance_type=instance_type, image_id= t2_micro_ami)
