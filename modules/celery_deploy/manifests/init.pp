class celery_deploy{

  $rabbit_ip = '192.168.33.19'
  $rabbit_user = 'deploy_rabbit'
  $rabbit_pass = 'hewhomustnotbenamed'
  $rabbit_vhost = 'elmer_fudd'
  $nosql_ip = '191.168.33.16'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin']
  $deploy_home = '/home/vagrant'
  $script_name = 'stream_analysis.py'
  $tasks_script = 'tasks.py'
  $handler_name = 'mongodb_handler.py'
  $extra_packages = ''

  exec { 'apt-get_update':
    command => 'sudo apt-get update  || true',
    path => $path
  }

  exec { 'install_dependencies':
    command => 'sudo apt-get install -y python2.7-dev python-pip rabbitmq-server',
    path => $path,
    require => Exec['apt-get_update']
  }

  exec {'install_celery':
    command => "sudo pip install Celery ${extra_packages}",
    path => $path,
    require => Exec['install_dependencies']
  }

  file { "${deploy_home}/${script_name}":
    content => template("celery_deploy/${script_name}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${tasks_script}":
    content => template("celery_deploy/${tasks_script}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${handler_name}":
    source => "puppet:///modules/celery_deploy/${handler_name}",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/const.py":
    source => "puppet:///modules/celery_deploy/const.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/data_gen.py":
    source => "puppet:///modules/celery_deploy/data_gen.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/nosql_handler.py":
    source => "puppet:///modules/celery_deploy/nosql_handler.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }
  
  file { "/etc/rabbitmq/rabbitmq-env.conf":
    content => template("celery_deploy/rabbitmq-env.conf.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery'],
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
