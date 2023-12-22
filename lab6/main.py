import boto3


def main():
    # Step 1: Set up the Boto3 session
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='ap-south-1'  # e.g., 'us-west-1'
    )

    # Step 2: Create a new application on Elastic Beanstalk
    eb = session.client('elasticbeanstalk')

    response = eb.create_application(
        ApplicationName='MyUniqueApp',
        Description='My personal web application'
    )

    # Step 4: Create an environment for the application
    env_response = eb.create_environment(
        ApplicationName='MyUniqueApp',
        EnvironmentName='MyUniqueApp-env',
        SolutionStackName='64bit Amazon Linux 2023 v4.0.4 running Python 3.9',
        VersionLabel='v1',
        OptionSettings=[
            {
                'Namespace': 'aws:autoscaling:launchconfiguration',
                'OptionName': 'InstanceType',
                'Value': 't2.micro'
            },
        ]
    )

    # Step 5: Configure CloudFront
    cloudfront = session.client('cloudfront')

    cf_response = cloudfront.create_distribution(
        DistributionConfig={
            'CallerReference': 'MyUniqueApp',
            'Origins': {
                'Quantity': 1,
                'Items': [
                    {
                        'Id': 'MyUniqueAppS3Origin',
                        'DomainName': 'cs351-lab3.s3.amazonaws.com',
                        'S3OriginConfig': {
                            'OriginAccessIdentity': ''
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'MyUniqueAppS3Origin',
                'ViewerProtocolPolicy': 'redirect-to-https',
                'MinTTL': 3600,
                'ForwardedValues': {
                    'QueryString': True,
                    'Cookies': {
                        'Forward': 'all'
                    }
                },
                'TrustedSigners': {
                    'Enabled': False,
                    'Quantity': 0
                },
            },
            'Comment': 'CloudFront Distribution for MyUniqueApp',
            'Enabled': True
        }
    )

    print("Deployment completed!")


if __name__ == '__main__':
    main()