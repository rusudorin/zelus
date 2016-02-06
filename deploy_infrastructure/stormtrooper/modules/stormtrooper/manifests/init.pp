class stormtrooper{

  $rabbit_ip = '$templ_rabbit_ip'
  $rabbit_user = '$templ_rabbit_user'
  $rabbit_pass = '$templ_rabbit_pass'
  $rabbit_vhost = '$templ_rabbit_vhost'
  $nosql_ip = '$templ_nosql_ip'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin']
  $deploy_home = '$templ_deploy_home'
  $script_name = 'stream_analysis.py'
  $tasks_script = 'tasks.py'
  $handler_name = '$templ_handler_name'
  $extra_packages = '$templ_extra_packages'

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
    content => template("stormtrooper/${script_name}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${tasks_script}":
    content => template("stormtrooper/${tasks_script}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${handler_name}":
    source => "puppet:///modules/stormtrooper/${handler_name}",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/const.py":
    source => "puppet:///modules/stormtrooper/const.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/data_gen.py":
    source => "puppet:///modules/stormtrooper/data_gen.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/nosql_handler.py":
    source => "puppet:///modules/stormtrooper/nosql_handler.py",
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

}
