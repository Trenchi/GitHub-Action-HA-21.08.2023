#! /bin/bash

sudo su
sudo apt update
sudo apt upgrade
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo mv index.html /var/www/html
sudo chown www-data:www-data /var/www/html
sudo chown www-data:www-data /var/www/html/index.html
sudo rm -r index.html
touch FERTIG