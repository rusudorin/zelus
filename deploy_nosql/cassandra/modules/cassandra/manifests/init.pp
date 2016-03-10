class cassandra{

  $cassandra_version = "3.3"
  $cassandra_ftp = "http://archive.apache.org/dist/cassandra/${cassandra_version}/apache-cassandra-${cassandra_version}-bin.tar.gz"
  $cassandra_home = "/home/$templ_user/cassandra"
  $home_folder = "/home/$templ_user"
  $cassandra_tarball = "cassandra.tar.gz"
  $seeds_list = "$templ_seeds_list"
  $listen_address = "$templ_listen_address"
  $rpc_address = "$templ_rpc_address"
  $cluster_name = "Benchmark Cluster"
  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']

  file { "$cassandra_home":
    ensure => "directory",
    owner => opennebula,
    group => opennebula,
  }

  exec { "download_cassandra":
    command => "wget ${cassandra_ftp} -O $cassandra_home/$cassandra_tarball --read-timeout=5 --tries=0",
    timeout => 1800,
    path => $path,
    creates => "$cassandra_home/$cassandra_tarball",
    require => Exec["install_java"]
  }

  exec { "add_java_repo":
    command => "sudo add-apt-repository -y ppa:openjdk-r/ppa",
    path => $path,
  }

  exec { 'apt-get_update':
    command => 'sudo apt-get update || true',
    path => $path,
    require => Exec["add_java_repo"]
  }

  exec { 'install_java':
    command => 'sudo apt-get install -y openjdk-8-jdk',
    path => $path,
    require => Exec['apt-get_update']
  }

  exec { 'unarchive':
    command => "tar xvzf ${cassandra_home}/cassandra.tar.gz -C ${cassandra_home} --strip-components=1",
    path => $path,
    creates => "${cassandra_home}/apache-cassandra-${cassandra_version}",
    require => Exec['download_cassandra']
  }

  file { "/var/lib/cassandra":
    owner => $templ_user,
    group => $templ_user,
    ensure => "directory",
  }

  file { "/var/log/cassandra":
    owner => $templ_user,
    group => $templ_user,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/data":
    owner => $templ_user,
    group => $templ_user,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/commitlog":
    owner => $templ_user,
    group => $templ_user,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/saved_caches":
    owner => $templ_user,
    group => $templ_user,
    ensure => "directory",
  }

  exec { 'set_java': command => '/bin/echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64" >> /home/$templ_user/.profile' }
  exec { 'set_cassandra': command => '/bin/echo "export CASSANDRA_HOME=${cassandra_home}" >> /home/$templ_user/.profile' }
  exec { 'set_path' :command => '/bin/echo "export PATH=\$PATH:\$CASSANDRA_HOME/bin" >> /home/$templ_user/.profile' }

  file { "${cassandra_home}/conf/cassandra.yaml":
    content => template("cassandra/cassandra.yaml.erb"),
    owner => root,
    group => root,
    require => Exec['unarchive']
  }

  exec { 'run_cassandra':
    command => "sudo sh ${cassandra_home}/bin/cassandra &",
    user => $templ_user,
    path => $path,
    require => File["${cassandra_home}/conf/cassandra.yaml"]
  }

  file { "${home_folder}/cpu_usage.sh":
    source => "puppet:///modules/cassandra/cpu_usage.sh",
    owner => root,
    group => root,
    require => Exec['unarchive']
  }

  file { "${home_folder}/cpu_load.sh":
    source => "puppet:///modules/cassandra/cpu_load.sh",
    owner => root,
    group => root,
    require => Exec['unarchive']
  }

  file {"/etc/supervisor/supervisord.conf":
    content => template("cassandra/supervisord.conf.erb"),
    owner => root,
    group => root,
    require => Exec['unarchive']
  }

  exec {"update_supervisor":
    command => "supervisorctl update",
    path => $path,
    require => File["/etc/supervisor/supervisord.conf"]
  }

}
