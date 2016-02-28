import argparse
import sys
import subprocess
import const

global NoSQLHandler


def get_rand_string(granularity):
    """
    get a random string
    """

    script_cmd = "python data_gen.py --size %d " % granularity
    return subprocess.check_output(script_cmd, shell=True).strip()


def set_environment(nosql):
    """
    Sets the correct imports according to the chosen nosql datastore
    """
    global NoSQLHandler
    if nosql == 'cassandra':
        from nosql_handlers.cassandra_handler import CassandraHandler as NoSQLHandler
    elif nosql == 'mongodb':
        from nosql_handlers.mongodb_handler import MongoDBHandler as NoSQLHandler
    elif nosql == 'riak':
        from nosql_handlers.riak_handler import RiakHandler as NoSQLHandler
    elif nosql == 'redis':
        from nosql_handlers.redis_handler import RedisHandler as NoSQLHandler
    elif nosql == 'bigcouch':
        from nosql_handlers.bigcouch_handler import BigCouchHandler as NoSQLHandler
    elif nosql == 'hbase':
        from nosql_handlers.hbase_handler import HBaseHandler as NoSQLHandler


def do_populate(ip_list, granularity, total_size, keyspace, columns, nosql):
    # basic checks

    if not ip_list:
        print "No ips"
        sys.exit(1)

    if not granularity:
        print "No granularity"
        sys.exit(2)

    if not total_size:
        print "No total_size"
        sys.exit(3)

    if not keyspace:
        print "No keyspace"
        sys.exit(4)

    if columns > total_size:
        print "Cannot have more columns than the total number of bytes"
        sys.exit(5)

    if nosql not in const.nosql_list:
        print "NoSQL datastore not supported"
        sys.exit(5)

    set_environment(nosql)

    # get the session
    nosql = NoSQLHandler(ip_list)

    i = 1
    while i * granularity <= total_size:

        # if the item was not added then do not increment the counter
        if nosql.perform_write(granularity):
            i += 1
