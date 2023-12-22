#cloud-boothook
#!/bin/bash
sudo yum install -y python flask
sudo service httpd start
aws s3 sync s3://lab-bucket-minshu/ /var/www/html/