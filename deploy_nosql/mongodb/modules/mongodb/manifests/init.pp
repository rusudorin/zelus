class mongodb{

  $bind_ip = "$templ_bind_ip"
  $replica_set_name = "$templ_replica_set_name"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']

  exec { "add_key":
    command => "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927",
    path => $path,
    user => root
  }

  exec { "add_mongo_repo":
    command => 'echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list',
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
    logoutput => on_failure,
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

  exec { 'set_java': command => '/bin/echo "export LC_ALL=C" >> /home/opennebula/.profile' }

}
