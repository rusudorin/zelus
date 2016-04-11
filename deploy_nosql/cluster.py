import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config


def set_mongo_cluster(user, arguments=''):
    for ip in config.mongo_secondary_ips:

        action = 'mongo ' + config.mongo_primary_ip + ':27017 < rs.add("' + ip + ':27017")'
        os.system("ssh " + arguments + " " + user + "@" + config.mongo_primary_ip + " " + "'" + action + "'")


def set_redis_cluster(user, arguments=''):
    action = "/home/" + user + "/redis-3.0.7/src/redis-trib.rb create "

    for ip in config.redis_ips:
        action += ip + ":6379 "
        action += " < yes"

    os.system("ssh " + arguments + " " + user + "@" + config.redis_ips[0] + " " + "'" + action + "'")


def set_riak_cluster(user, arguments=''):

    action_base = "riak-admin cluster join "

    for ip in config.riak_ips:

        action = action_base + "riak@" + ip
        os.system("ssh " + arguments + " " + user + "@" + config.riak_ips[0] + " " + "'" + action + "'")

    action = "riak-admin cluster plan"
    os.system("ssh " + arguments + " " + user + "@" + config.riak_ips[0] + " " + "'" + action + "'")

    action = "riak-admin cluster commit"
    os.system("ssh " + arguments + " " + user + "@" + config.riak_ips[0] + " " + "'" + action + "'")


def set_bigcouch_cluster(user, arguments=''):

    for ip in config.bigcouch_ips:

        action = "curl -X PUT http://0.0.0.0:5986/nodes/bigcouch@" + ip + " -d {}"

        os.system("ssh " + arguments + " " + user + "@" + config.bigcouch_ips[0] + " " + "'" + action + "'")
