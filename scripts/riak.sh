curl https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | sudo bash
sudo apt-get install riak=2.1.1-1

sudo sed -i 's/127.0.0.1/192.168.33.15/g' /etc/riak/riak.conf

riak stop
riak start
