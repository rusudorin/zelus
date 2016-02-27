class hbase {

  $path = ['/usr/bin', '/usr', '/usr/sbin', '/bin', '/sbin']
  $hostname = "$templ_hostname"
  $ip_address = "$templ_ip_address"
  $regionservers = "$templ_regionservers"
  $hbase_sites = "$hbase_sites"

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
    command => 'sudo apt-get install -y openjdk-8-jdk curl',
    path => $path,
    require => Exec['apt-get_update']
  }

  exec { 'set_java':
    command => '/bin/echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64" >> /etc/environment',
    path => $path,
    require => Exec['install_java']
  }

  exec { 'update_env':
    command => 'sh /etc/environment',
    path => $path,
    require => Exec['set_java']
  }

  exec { 'add_cloudera_repo':
    command => 'echo "deb http://archive.cloudera.com/debian maverick-cdh3 contrib" >> /etc/apt/sources.list.d/cloudera.list',
    path => $path,
    require => Exec['update_env']
  }

  exec { 'add_cloudera_repo2':
    command => 'echo "deb-src http://archive.cloudera.com/debian maverick-cdh3 contrib" >> /etc/apt/sources.list.d/cloudera.list',
    path => $path,
    require => Exec['add_cloudera_repo']
  }

  exec {'add_cloudera_key':
    command => 'curl -s http://archive.cloudera.com/debian/archive.key | sudo apt-key add -',
    path => $path,
    require => Exec['add_cloudera_repo2']
  }

  exec { 'apt-get_update2':
    command => 'sudo apt-get update || true',
    path => $path,
    require => Exec["add_cloudera_key"]
  }

  exec { 'install_hadoop':
    command => 'sudo apt-get install -y hadoop-0.20',
    path => $path,
    require => Exec['apt-get_update2']
  }

  exec { 'install_hbase':
    command => 'sudo apt-get install -y hadoop-hbase',
    path => $path,
    require => Exec['install_hadoop']
  }

  exec { 'install_hbase_master':
    command => 'sudo apt-get install -y hadoop-hbase-master',
    path => $path,
    require => Exec['install_hbase']
  }

   exec { 'set_hostname':
    command => "sudo /bin/echo '${hostname}' > /etc/hostname",
    user => root,
    path => $path,
    require => Exec['install_hbase_master']
  }

  exec { 'set_ip_address':
    command => "sudo /bin/echo '${ip_address} ${hostname}' >> /etc/hosts",
    path => $path,
    require => Exec['set_hostname']
  }

  file { "/etc/hbase/conf/hbase-site.xml":
    content => template("hbase/hbase-site.xml.erb"),
    owner => hbase,
    group => hbase,
    require => Exec['install_hbase']
  }

  file { "/etc/hbase/conf/regionservers":
    content => template("hbase/regionservers.erb"),
    owner => hbase,
    group => hbase,
    require => Exec['install_hbase']
  }
}
