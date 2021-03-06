class redis{

  $bind_ip = "$templ_bind_ip"
  $home_folder = "$templ_home_folder"
  $redis_version = "redis-3.0.7"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin']

  exec {"install_make":
    command => "sudo apt-get install -y make rubygems ; gem install redis",
    path => $path
  }

  exec {"download_redis":
    command => "wget http://download.redis.io/releases/$redis_version.tar.gz -O $$home_folder/${redis_version}.tar.gz",
    timeout => 1800,
    path => $path,
    creates => "$home_folder/$redis_version.tar.gz",
    require => Exec['install_make']
  }

  exec {'unarchive':
    command => "tar xzf ${home_folder}/${redis_version}.tar.gz -C ${home_folder}",
    path => $path,
    creates => "${home_folder}/${redis_version}",
    require => Exec['download_redis']
  } 

  exec {'make':
    command => "make",
    path => $path,
    cwd => "${home_folder}/${redis_version}",
    require => Exec['unarchive']
  }

  file {"${home_folder}/${redis_version}/redis.conf":
    content => template("redis/redis.conf.erb"),
    owner => root,
    group => root,
    require => Exec['make']
  }

  exec {'run_redis':
    command => "${home_folder}/${redis_version}/src/redis-server ${home_folder}/${redis_version}/redis.conf &",
    path => $path,
    require => File["${home_folder}/${redis_version}/redis.conf"]
  }

  file { "${home_folder}/cpu_usage.sh":
    source => "puppet:///modules/redis/cpu_usage.sh",
    owner => root,
    group => root,
    require => Exec['run_redis']
  }

  file { "${home_folder}/cpu_load.sh":
    source => "puppet:///modules/redis/cpu_load.sh",
    owner => root,
    group => root,
    require => Exec['run_redis']
  }

  file {"/etc/supervisor/supervisord.conf":
    content => template("redis/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => Exec['run_redis']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }

}

