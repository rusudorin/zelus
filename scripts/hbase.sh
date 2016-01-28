# download hbase
wget http://ftp.tudelft.nl/apache/hbase/hbase-0.94.27/hbase-0.94.27.tar.gz

# unarchive
tar -xzvf hbase-0.94.27.tar.gz

# move to a more manageable location
mv hbase-0.94.27 /home/vagrant/hbase

# install JAVA
sudo add-apt-repository -y ppa:openjdk/ppa
sudo apt-get update
sudo apt-get install -y openjdk-7-jdk

# set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64

export JAVA_HOME=/usr/
echo "export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64" >> /etc/profile
#echo "export JAVA_HOME=/usr/" >> /etc/profile

# give ownership to the vagrant user for the folder
sudo chown -R vagrant /home/vagrant/hbase

sudo sed -i 's/<configuration>/ /g' /home/vagrant/hbase/conf/hbase-site.xml
sudo sed -i 's/</configuration>/ /g' /home/vagrant/hbase/conf/hbase-site.xml

# change folder
cd /home/vagrant/

# run hbase
# ./hbase/bin/start-hbase.sh
