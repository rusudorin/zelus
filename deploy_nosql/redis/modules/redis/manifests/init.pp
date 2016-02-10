class redis{

  $bind_ip = "$templ_bind_ip"
  $redis_home = "$templ_home"
  $redis_version = "redis-3.0.7"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin']

  exec {"install_make":
    command => "sudo apt-get install -y make rubygems ; gem install redis",
    path => $path
  }

  exec {"download_redis":
    command => "wget http://download.redis.io/releases/$redis_version.tar.gz -O $redis_home/${redis_version}.tar.gz",
    timeout => 1800,
    path => $path,
    creates => "$redis_home/$redis_version.tar.gz",
    require => Exec['install_make']
  }

  exec {'unarchive':
    command => "tar xzf ${redis_home}/${redis_version}.tar.gz -C ${redis_home}",
    path => $path,
    creates => "${redis_home}/${redis_version}",
    require => Exec['download_redis']
  } 

  exec {'make':
    command => "make",
    path => $path,
    cwd => "${redis_home}/${redis_version}",
    require => Exec['unarchive']
  }

  file {"${redis_home}/${redis_version}/redis.conf":
    content => template("redis/redis.conf.erb"),
    owner => root,
    group => root,
    require => Exec['make']
  }

  exec {'run_redis':
    command => "${redis_home}/${redis_version}/src/redis-server ${redis_home}/${redis_version}/redis.conf &",
    path => $path,
    require => File["${redis_home}/${redis_version}/redis.conf"]
  }

}

