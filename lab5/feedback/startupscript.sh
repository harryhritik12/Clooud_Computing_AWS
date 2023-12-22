sudo yum install -y python pip
AWS_ACCESS_KEY='AKIARDIRXYDST64IV3OJ'
AWS_SECRET_KEY = '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'

sudo aws configure set aws_access_key_id $AWS_ACCESS_KEY
sudo aws configure set aws_secret_access_key $AWS_SECRET_KEY,
sudo aws configure set default.region ap-sout-1
sudo aws configure set default.output json

aws s3 sync s3://lab-bucket-minshu/ /var/www/html/

sudo pip install flask 
python -m pip install mysql-connector-python

flask run 
