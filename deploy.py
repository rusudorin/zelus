from multiprocessing import Process
import deploy_infrastructure.deploy_helper as di
import deploy_nosql.deploy_helper as dn
import config
import const


def stormtrooper(lots_of_args):
    p = Process(target=deploy_stormtrooper, args=lots_of_args)
    p.start()
    return p


# launch an emperor node
def deploy_emperor(user, host):
    d = {
            "templ_rabbit_ip": host,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost
        }
    di.deploy('emperor', user, host, d)


# launch a stormtrooper
def deploy_stormtrooper(user, host, nosql, worker_name, concurrency, worker_number):

    emperor_ip = 0

    for key in config.worker_emperors:
        if host in config.worker_emperors[key]:
            emperor_ip = key
            break

    extra_pip_packages = {
        "mongodb": "pymongo",
        "cassandra": "pycassa",
        "hbase": "happybase",
        "redis": "redis",
        "riak": "riak",
        "bigcouch": "couchdbkit"
    }

    extra_apt_packages = {
        "mongodb": "",
        "cassandra": "",
        "hbase": "",
        "redis": "",
        "riak": "build-essential libssl-dev libffi-dev python-dev",
        "bigcouch": ""
    }

    if nosql not in const.nosql_list:
        return "Nope"

    nosql_string = ''
    for ip in config.nosql_ips:
        nosql_string += ip + ","

    nosql_string = nosql_string[:-1]

    d = {
            "templ_rabbit_ip": emperor_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost,
            "templ_nosql_ip": nosql_string,
            "templ_deploy_home": "/home/opennebula",  # TODO: temporary, change back once not using opennebula
            # "templ_deploy_home": "/home/" + user,
            "templ_handler_name": nosql + "_handler",
            "templ_handler_class": const.nosql_classes[nosql],
            "templ_extra_pip_packages": extra_pip_packages[nosql],
            "templ_extra_apt_packages": extra_apt_packages[nosql],
            "templ_worker_name": worker_name,
            "templ_worker_number": range(0, worker_number),
            "templ_concurrency": concurrency,
            "templ_current_ip": host,
            "templ_user_ip": config.user_ip
        }

    di.deploy('stormtrooper', user, host, d)


# launch a mongodb node
def deploy_mongodb(user, host):

    d = {
        "templ_bind_ip": host,
        "templ_replica_set_name": const.keyspace_name,
        "templ_home_folder": "/home/" + user
    }

    dn.deploy('mongodb', user, host, d)


# launch a redis node
def deploy_redis(user, host):

    d = {
        "templ_bind_ip": host,
        "templ_home_folder": "/home/" + user
    }

    dn.deploy('redis', user, host, d)


# launch a riak node
def deploy_riak(user, host):

    d = {
            "templ_bind_ip": host,
            "templ_home_folder": "/home/" + user
        }

    dn.deploy('riak', user, host, d)


# launch cassandra node
def deploy_cassandra(user, host):

    seeds = ""
    for ip in config.cassandra_ips:
        seeds += ip + ","

    d = {
            "templ_user": user,
            "templ_listen_address": host,
            "templ_rpc_address": host,
            "templ_seeds_list": seeds,
        }

    dn.deploy('cassandra', user, host, d)


# launch bigcouch
def deploy_bigcouch(user, host):

    d = {
            "templ_home_folder": "/home/" + user
        }
    dn.deploy('bigcouch', user, host, d)


# launch hbase
def deploy_hbase(user, host):

    regionservers = ''
    for ip in config.hbase_ips:
        regionservers += ip + '\n'

    # setting hbase in distributed mode
    hbase_sites = "<property>\n  <name>hbase.cluster.distributed</name>\n  <value>true</value>\n</property>"

    hbase_sites += '\n'

    # adding all zookeepers
    hbase_sites += "<property>\n  <name>hbase.zookeeper.quorum</name>\n  <value>"

    zookeeper_ips = ''
    for ip in config.hbase_ips:
        zookeeper_ips += ip + ','
    zookeeper_ips = zookeeper_ips[:-1]

    hbase_sites += zookeeper_ips
    hbase_sites += "</value>\n</property>"

    # adding zookeeper data dir
    hbase_sites += "<property>\n  <name>hbase.zookeeper.property.dataDir</name>\n" \
                   "  <value>/usr/local/zookeeper</value>\n</property>"

    d = {
            "templ_hostname": const.hbase_hostname,
            "templ_ip_address": host,
            "templ_regionservers": regionservers,
            "templ_hbase_sites": hbase_sites,
            "templ_home_folder": "/home/" + user
        }
    dn.deploy('hbase', user, host, d)
