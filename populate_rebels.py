import const
import config
import subprocess
import sys

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
    else:
        raise Exception('No such NoSQL')


def do_populate(nosql, granularity, total_size):
    # basic checks
    if not granularity:
        print "No granularity"
        sys.exit(1)

    if not total_size:
        print "No total_size"
        sys.exit(2)

    if nosql not in const.nosql_list:
        print "NoSQL datastore not supported"
        sys.exit(3)

    set_environment(nosql)

    # get the session
    nosql = NoSQLHandler(config.nosql_ips)

    print "Populating rebels"
    i = 1
    while i * granularity <= total_size:

        # if the item was not added then do not increment the counter
        if nosql.perform_write(granularity):
            i += 1

    print "Finished populating"
