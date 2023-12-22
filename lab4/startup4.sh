#!/bin/bash

# Update and install httpd (Amazon Linux 2 uses httpd)
yum update -y
yum install -y httpd

# Start the httpd service
systemctl start httpd
systemctl enable httpd

# Ensure permissions are set correctly for the web directory
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www

# Sync website files from S3 bucket root to the web directory
aws s3 sync s3://lab-bucket-minshu/ /var/www/html/

# Restart the httpd service
systemctl restart httpd