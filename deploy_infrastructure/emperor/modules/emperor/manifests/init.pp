class emperor{

  $rabbit_ip = '$templ_rabbit_ip'
  $rabbit_user = '$templ_rabbit_user'
  $rabbit_pass = '$templ_rabbit_pass'
  $rabbit_vhost = '$templ_rabbit_vhost'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']

  $enhancers = ['python2.7-dev', 'python-pip', 'rabbitmq-server']
  package{ $enhancers: ensure => 'installed' }

  file { "/etc/rabbitmq/rabbitmq-env.conf":
    content => template("emperor/rabbitmq-env.conf.erb"),
    owner => root,
    group => root,
    require => Package[$enhancers],
    notify => Service['rabbitmq-server']
  }

  service {'rabbitmq-server':
    ensure => 'running',
    enable => 'true',
    require => Exec['install_dependencies']
  }

  exec {'create_user':
    command => "sudo rabbitmqctl add_user ${rabbit_user} ${rabbit_pass}",
    user => root,
    path => $path,
    require => File['/etc/rabbitmq/rabbitmq-env.conf']
  }

  exec {'create_vhost':
    command => "sudo rabbitmqctl add_vhost ${rabbit_vhost}",
    path => $path,
    require => Exec['create_user'] 
  }

  exec {'create_permissions':
    command => "sudo rabbitmqctl set_permissions -p ${rabbit_vhost} ${rabbit_user} \".*\" \".*\" \".*\"",
    path => $path,
    require => Exec['create_vhost']
  }

}
