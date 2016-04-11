import const
import config
import sys


def get_environment(nosql):
    """
    Sets the correct imports according to the chosen nosql datastore
    """
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
    return NoSQLHandler


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

    handler = get_environment(nosql)

    # get the session from any nosql ip
    for ip in config.nosql_ips:
        nosql = handler(ip)
        break

    print "Populating rebels"
    i = 1
    while i * granularity <= total_size:

        # if the item was not added then do not increment the counter
        if nosql.perform_write(granularity):
            i += 1

    print "Finished populating"
