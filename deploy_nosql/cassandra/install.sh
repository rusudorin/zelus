sudo apt-get update
sudo apt-get install -y python2.7-dev python-pip puppet supervisor software-properties-common python-software-properties
puppet apply --modulepath=modules/ manifests/init.pp
