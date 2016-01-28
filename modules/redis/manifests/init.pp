class redis{

  $bind_ip = "192.168.33.16"
  $redis_version = "2.8.9"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin']

  exec {"add_key":
    command => 'wget -q -O - http://www.dotdeb.org/dotdeb.gpg | sudo apt-key add -',
    user => root,
    path => $path,
    creates => "/home/vagrant/redis-${redis_version}.tar.gz"
  }

  exec { 'apt-get_update':
    command => 'sudo apt-get update || true',
    path => $path,
    require => Exec['add_key']
  }

  exec { "install_redis":
    command => 'sudo apt-get install -y redis-server',
    path => $path,
    user => root,
    require => Exec['apt-get_update']
  }

  file { "/etc/redis/redis.conf":
    content => template("redis/redis.conf.erb"),
    owner => root,
    group => root,
    require => Exec['install_redis'],
    notify => Service['redis-server']
  }

  service { "redis-server":
    ensure => "running",
    enable => "true",
    require => File['/etc/redis/redis.conf']
  }

}
