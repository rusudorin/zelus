class stormtrooper{

  $rabbit_ip = '$templ_rabbit_ip'
  $rabbit_user = '$templ_rabbit_user'
  $rabbit_pass = '$templ_rabbit_pass'
  $rabbit_vhost = '$templ_rabbit_vhost'
  $nosql_ip = '$templ_nosql_ip'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']
  $deploy_home = '$templ_deploy_home'
  $tasks_script = 'tasks.py'
  $handler_name = '$templ_handler_name'
  $handler_class = '$templ_handler_class'
  $extra_pip_packages = '$templ_extra_pip_packages'
  $extra_apt_packages = '$templ_extra_apt_packages'
  $worker_name = '$templ_worker_name'
  $worker_number = $templ_worker_number
  $concurrency = '$templ_concurrency'
  $current_ip = '$templ_current_ip'
  $user_ip = '$templ_user_ip'

  exec { 'apt-get_update':
    command => 'sudo apt-get update  || true',
    path => $path
  }

  exec { 'install_dependencies':
    command => "sudo apt-get install -y python2.7-dev python-pip supervisor ${extra_apt_packages}",
    path => $path,
    require => Exec['apt-get_update']
  }

  exec {'install_celery':
    command => "sudo pip install Celery ${extra_pip_packages}",
    path => $path,
    require => Exec['install_dependencies']
  }

  celery_file{ $worker_number:}

  define celery_file (){
    $worker_nb = $title
    file { "stream_analysis${title}.py":
      content => template("stormtrooper/stream_analysis.py.erb"),
      path => "${deploy_home}/stream_analysis${title}.py",
      owner => root,
      group => root,
      require => Exec['install_celery']
    }
  }

  file { "${deploy_home}/${tasks_script}":
    content => template("stormtrooper/${tasks_script}.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  file { "${deploy_home}/${handler_name}.py":
    source => "puppet:///modules/stormtrooper/${handler_name}.py",
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

  file {"/etc/supervisor/supervisord.conf":
    content => template("stormtrooper/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => Exec['install_celery']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }

}
