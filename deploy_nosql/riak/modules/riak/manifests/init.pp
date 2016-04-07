class riak{

  $bind_ip = "$templ_bind_ip"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin']
  $home_folder = '$templ_home_folder'

  exec {"add_repo":
    command => 'curl https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | sudo bash',
    path => $path,
    user => root
  }

  exec { "install_riak":
    command => 'sudo apt-get install -y riak',
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

  file { "${home_folder}/cpu_usage.sh":
    source => "puppet:///modules/riak/cpu_usage.sh",
    owner => root,
    group => root,
    require => File['/etc/riak/riak.conf']
  }

  file { "${home_folder}/cpu_load.sh":
    source => "puppet:///modules/riak/cpu_load.sh",
    owner => root,
    group => root,
    require => File['/etc/riak/riak.conf']
  }

  file {"/etc/supervisor/supervisord.conf":
    content => template("riak/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => File['/etc/riak/riak.conf']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }

}
