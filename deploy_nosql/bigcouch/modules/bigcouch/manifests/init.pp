class bigcouch{
  $home_folder = '$templ_home_folder'
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin']

  $enhancers = [ 'erlang-reltool', 'libicu-dev', 'libmozjs-dev', 'make', 'git', 'libicu-dev', 'erlang-base', 'erlang-dev', 'erlang-eunit', 'erlang-nox', 'libmozjs-dev']
  package { $extra_apt_packages: ensure => 'installed' }

  exec {"clone_repo":
    command => "git clone https://github.com/cloudant/bigcouch",
    cwd => "${home_folder}",
    user => root,
    path => $path,
    require => Package[$enhancers]
  }

  exec {'configure':
    command => "sh configure",
    cwd => "${home_folder}/bigcouch",
    user => root,
    path => $path,
    require => Exec['clone_repo'],
  }

  exec {"make":
    command => "make",
    cwd => "${home_folder}/bigcouch",
    user => root,
    path => $path,
    require => Exec['configure']
  }

  exec {"make_install":
    command => "make install",
    cwd => "${home_folder}/bigcouch",
    user => root,
    path => $path,
    require => Exec['make']
  }

  file {"/opt/bigcouch/etc/default.ini":
    source => "puppet:///modules/bigcouch/default.ini",
    owner => root,
    group => root,
    require => Exec['make_install']
  }

  exec {'run':
    command => "${home_folder}/bigcouch/rel/bigcouch/bin/bigcouch &",
    user => root,
    path => $path,
    require => File['/opt/bigcouch/etc/default.ini']
  }

  file { "${home_folder}/cpu_usage.sh":
    source => "puppet:///modules/bigcouch/cpu_usage.sh",
    owner => root,
    group => root,
    require => Exec['make_install']
  }

  file { "${home_folder}/cpu_load.sh":
    source => "puppet:///modules/bigcouch/cpu_load.sh",
    owner => root,
    group => root,
    require => Exec['make_install']
  }

  file {"/etc/supervisor/supervisord.conf":
    content => template("bigcouch/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => Exec['make_install']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }
}
