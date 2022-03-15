#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd.service
echo "Hello world, from $(hostname -f)" > /var/www/html/index.html