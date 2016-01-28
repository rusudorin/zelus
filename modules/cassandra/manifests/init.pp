class cassandra{

  $cassandra_version = "2.0.16"
  $cassandra_ftp = "ftp://mirror.nl.webzilla.com/apache/cassandra/${cassandra_version}/apache-cassandra-${cassandra_version}-bin.tar.gz"
  $cassandra_home = "/vagrant/cassandra"
  $cassandra_tarball = "cassandra.tar.gz"
  $seeds_list = "192.168.33.16"
  $listen_address = "192.168.33.16"
  $rpc_address = "192.168.33.16"
  $cluster_name = "Benchmark Cluster"
  $path = ['/usr/bin', '/bin']

  file { "$cassandra_home":
    ensure => "directory",
  }

  exec { "download_cassandra":
    command => "wget ${cassandra_ftp} -O $cassandra_home/$cassandra_tarball --read-timeout=5 --tries=0",
    timeout => 1800,
    path => $path,
    creates => "$cassandra_home/$cassandra_tarball",
    require => File["$cassandra_home"]
  }

  exec { "add_java_repo":
    command => "sudo add-apt-repository -y ppa:openjdk/ppa",
    path => $path,
  }

  exec { 'apt-get_update':
    command => 'sudo apt-get update || true',
    path => $path,
    require => Exec["add_java_repo"]
  }

  exec { 'install_java':
    command => 'sudo apt-get install -y openjdk-7-jdk',
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
    owner => root,
    group => root,
    ensure => "directory",
  }

  file { "/var/log/cassandra":
    owner => root,
    group => root,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/data":
    owner => root,
    group => root,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/commitlog":
    owner => root,
    group => root,
    ensure => "directory",
  }

  file { "/var/lib/cassandra/saved_caches":
    owner => root,
    group => root,
    ensure => "directory",
  }

  exec { 'set_java': command => '/bin/echo "export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64" >> /home/vagrant/.profile' }
  exec { 'set_cassandra': command => '/bin/echo "export CASSANDRA_HOME=${cassandra_home}" >> /home/vagrant/.profile' }
  exec { 'set_path' :command => '/bin/echo "export PATH=\$PATH:\$CASSANDRA_HOME/bin" >> /home/vagrant/.profile' }

  file { "${cassandra_home}/conf/cassandra.yaml":
    content => template("cassandra/cassandra.yaml.erb"),
    owner => vagrant,
    group => vagrant,
    require => Exec['unarchive']
  }

  exec { 'run_cassandra':
    command => "sudo sh ${cassandra_home}/bin/cassandra",
    user => root,
    path => $path,
    require => File["${cassandra_home}/conf/cassandra.yaml"]
  }

  exec { 'create_table':
    command => "echo /'create keyspace benchmark;/' | sudo sh ${cassandra_home}/bin/cassandra-cli --host ${listen_address} --port 9160",
    user => root,
    path => $path,
    require => Exec['run_cassandra']
  }

}
