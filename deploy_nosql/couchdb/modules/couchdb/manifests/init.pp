class couchdb{

  $bind_address = "bind_address = 192.168.33.16"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/sbin', '/usr/local/sbin', '/bin']

  exec { "install_couch":
    command => 'sudo apt-get install -y couchdb',
    path => $path,
    user => root
  }

  file { "/etc/couchdb/local.ini":
    content => template("couchdb/local.ini.erb"),
    owner => couchdb,
    group => couchdb,
    require => Exec['install_couch'],
    notify => Service['couchdb']
  }

  service { 'couchdb':
    ensure => "running",
    enable => "true",
    require => File['/etc/couchdb/local.ini']
  }

}
