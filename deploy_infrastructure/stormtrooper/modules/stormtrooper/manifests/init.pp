class stormtrooper{

  $rabbit_ip = '192.168.33.14'
  $rabbit_user = 'ndoye'
  $rabbit_pass = 'usmanescu'
  $rabbit_vhost = 'asa'
  $nosql_ip = '192.168.33.44'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin']
  $deploy_home = '/home/opennebula'
  $script_name = 'stream_analysis.py'
  $tasks_script = 'tasks.py'
  $handler_name = 'riak_handler.py'
  $extra_packages = ''

  exec { 'apt-get_update':
    command => 'sudo apt-get update  || true',
    path => $path
  }

  exec { 'install_dependencies':
    command => 'sudo apt-get install -y python2.7-dev python-pip',
    path => $path,
    require => Exec['apt-get_update']
  }

  exec {'install_celery':
    command => "sudo pip install Celery ${extra_packages}",
    path => $path,
    require => Exec['install_dependencies']
  }

file { "${deploy_home}/${script_name}":
    content => template("worker_deploy/${script_name}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${tasks_script}":
    content => template("worker_deploy/${tasks_script}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${handler_name}":
    source => "puppet:///modules/worker_deploy/${handler_name}",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/const.py":
    source => "puppet:///modules/worker_deploy/const.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/data_gen.py":
    source => "puppet:///modules/worker_deploy/data_gen.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/nosql_handler.py":
    source => "puppet:///modules/worker_deploy/nosql_handler.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

}
