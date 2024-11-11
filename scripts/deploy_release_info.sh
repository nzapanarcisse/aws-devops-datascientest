#!/bin/bash

# Update PATH
PATH=$PATH:/usr/local/bin/
yum install python3-pip -y
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
sudo yum install git -y 
rm -Rf alpinehelloworld || echo "folder already deleted"
rm -Rf /root/deployment || echo "folder already deleted"
git clone https://github.com/nzapanarcisse/aws-devops-datascientest.git ./alpinehelloworld
