# download cassandra archive
wget ftp://mirror.nl.webzilla.com/apache/cassandra/2.0.16/apache-cassandra-2.0.16-bin.tar.gz

# install JAVA
sudo add-apt-repository -y ppa:openjdk/ppa
sudo apt-get update
sudo apt-get install -y openjdk-7-jdk

# unarchive the archive (sic)
tar -xvzf apache-cassandra-2.0.16-bin.tar.gz

# move the folder to a more mangageable location
mv apache-cassandra-2.0.16 /home/vagrant/cassandra

# create Cassandra folders and give access
sudo mkdir /var/lib/cassandra
sudo mkdir /var/log/cassandra
sudo mkdir /var/lib/cassandra/data
sudo mkdir /var/lib/cassandra/commitlog
sudo mkdir /var/lib/cassandra/saved_caches
sudo chown -R $USER:$GROUP /var/lib/cassandra
sudo chown -R $USER:$GROUP /var/log/cassandra

# set Cassandra variables
export CASSANDRA_HOME=/home/vagrant/cassandra
export PATH=$PATH:$CASSANDRA_HOME/bin
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64
echo "export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64" >> /home/vagrant/.profile
echo "export CASSANDRA_HOME=/home/vagrant/cassandra" >> /home/vagrant/.profile
echo "export PATH=$PATH:$CASSANDRA_HOME/bin" >> /home/vagrant/.profile

# set the ip to the config file
sudo sed -i 's/localhost/\"192.168.33.11\"/g' /home/vagrant/cassandra/conf/cassandra.yaml
sudo sed -i 's/\"127.0.0.1\"/\"192.168.33.11\"/g' /home/vagrant/cassandra/conf/cassandra.yaml

# start cassandra
sudo sh /home/vagrant/cassandra/bin/cassandra 

echo "Waiting 10s"
sleep 10
echo "Waited 10s"

sudo touch /home/vagrant/cassandra/conf/cassandra.yaml

echo "create keyspace benchmark;" | sudo sh cassandra/bin/cassandra-cli --host 192.168.33.11 --port 9160
# create a default keyspace
# echo "create keyspace benchmark WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };" | cqlsh 192.168.33.10
