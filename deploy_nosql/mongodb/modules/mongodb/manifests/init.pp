class mongodb{

  $bind_ip = "$templ_bind_ip"
  $replica_set_name = "$templ_replica_set_name"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']
  $home_folder = "$templ_home_folder"

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

  file { "${home_folder}/cpu_usage.sh":
    source => "puppet:///modules/mongodb/cpu_usage.sh",
    owner => root,
    group => root,
    require => File['/etc/mongod.conf']
  }

  file { "${home_folder}/cpu_load.sh":
    source => "puppet:///modules/mongodb/cpu_load.sh",
    owner => root,
    group => root,
    require => File['/etc/mongod.conf']
  }

  file {"/etc/supervisor/supervisord.conf":
    content => template("mongodb/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => File['/etc/mongod.conf']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }

}
