class riak{

  $bind_ip = "$templ_bind_ip"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin'] 

  exec {"add_repo":
    command => 'curl https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | sudo bash',
    path => $path,
    user => root
  }

  exec { "install_riak":
    command => 'sudo apt-get install -y riak=2.1.1-1',
    user => root,
    path => $path,
    require => Exec['add_repo']
  }

  file { "/etc/riak/riak.conf":
    content => template("riak/riak.conf.erb"),
    owner => riak,
    group => riak,
    require => Exec['install_riak']
  }

  exec { "start_riak":
    command => 'sudo riak start',
    path => $path,
    require => File['/etc/riak/riak.conf']
  }

}
