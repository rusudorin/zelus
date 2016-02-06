sudo apt-get update
sudo apt-get install -y python2.7-dev python-pip puppet
puppet apply --modulepath=modules/ manifests/init.pp
