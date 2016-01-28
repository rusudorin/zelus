class mongodb{

  $bind_ip = "192.168.33.16"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin']

  exec { "add_key":
    command => "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10",
    path => $path,
    user => root
  }

  exec { "add_mongo_repo":
    command => 'echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list',
    path => $path,
    user => root,
    require => Exec['add_key']
  }

  exec { 'apt-get_update':
    command => 'sudo apt-get update  || true',
    path => $path,
    require => Exec['add_mongo_repo']
  }

  exec { 'install_mongo':
    command => 'sudo apt-get install -y mongodb-org',
    path => $path,
    user => root,
    require => Exec['apt-get_update']
  }

  file { "/etc/mongod.conf":
    content => template("mongodb/mongod.conf.erb"),
    owner => root,
    group => root,
    require => Exec['install_mongo'],
    notify => Service['mongod']
  }

  service { 'mongod':
    ensure => "running",
    enable => "true",
    require => File['/etc/mongod.conf']
  }

  exec { 'set_java': command => '/bin/echo "export LC_ALL=C" >> /home/vagrant/.profile' }

}
