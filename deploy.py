import deploy_infrastructure.deploy_helper as di
import deploy_nosql.deploy_helper as dn

import config
import const

# launch an emperor node
def deploy_emperor(user, host):
    d = {
            "templ_rabbit_ip": config.rabbit_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost
        }
    di.deploy('emperor', user, host, d)

# launch a stormtrooper
def deploy_stormtrooper(user, host, nosql, worker_name, concurrency, queue):

    if nosql not in const.nosql_list:
        return "Nope"

    d = {
            "templ_rabbit_ip": config.rabbit_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost,
            "templ_nosql_ip": config.nosql_ip,
            "templ_deploy_home": "/home/" + user,
            "templ_handler_name": nosql + "_handler",
            "templ_handler_class": const.nosql_classes[nosql],
            "templ_extra_package": "",
            "templ_worker_name": worker_name,
            "templ_concurrency": concurrency,
            "templ_consume_queue": queue,
            "templ_current_ip": host,
            "templ_user_ip": config.user_ip
        }

    di.deploy('stormtrooper', user, host, d)


# launch a mongodb node
def deploy_mongodb(user, host, replica_set):

    d = {
	"templ_bind_ip": host,
	"templ_replica_set_name": replica_set
    }

    dn.deploy('mongodb', user, host, d)

# launch a redis node
def deploy_redis(user, host):

    d = {
	"templ_bind_ip": host,
	"templ_home": "/home" + user,
    }

    dn.deploy('redis', user, host, d)

# launch a riak node
def deploy_riak(user, host):

    d = {
            "templ_bind_ip": host,
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
