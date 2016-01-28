# add key
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

# add mongo repo
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list

# update local package db
sudo apt-get update

# install mongo
sudo apt-get install -y mongodb-org

# bind ip
sudo sed -i 's/127.0.0.1/192.168.33.10/g' /etc/mongod.conf

# restart mongo
sudo service mongod restart
