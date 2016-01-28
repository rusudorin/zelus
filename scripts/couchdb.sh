# install from repo
sudo apt-get install -y couchdb

sudo sed -i 's/;bind_address/bind_address/g' /etc/couchdb/local.ini
sudo sed -i 's/127.0.0.1/192.168.33.10/g' /etc/couchdb/local.ini

sudo service couchdb restart
