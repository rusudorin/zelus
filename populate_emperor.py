from tasks import read_nosql, write_nosql, update_nosql, start_consuming, stop_consuming
from random import randint
from multiprocessing import Process
import config

global NoSQLHandler


# populate a queue with read tasks
def populate_queue_read(nosql, queue_name, amount):
    print "Populating %s..." % queue_name
    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    generated_timestamp_list = []
    timestamp_list = handler.get_timestamp_list()

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)
        generated_timestamp_list.append(timestamp_list[index-1])

    for i in range(0, len(generated_timestamp_list)):
        read_nosql.apply_async(args=[generated_timestamp_list[i]], queue=queue_name)
    print "Finished populating %s" % queue_name


# populate a queue with write tasks
def populate_queue_write(queue_name, amount, granularity, varying=False):
    print "Populating %s..." % queue_name

    for i in range(0, amount):
        if varying:
            write_size = randint(0, granularity)
        else:
            write_size = granularity

        write_nosql.apply_async(args=[write_size], queue=queue_name)

    print "Finished populating %s" % queue_name


# populate a queue with update tasks
def populate_queue_update(nosql, queue_name, amount, granularity, varying=False):
    print "Populating %s..." % queue_name
    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    timestamp_list = handler.get_timestamp_list()

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)

        if varying:
            write_size = randint(0, granularity)
        else:
            write_size = granularity

        update_nosql.apply_async(args=[timestamp_list[index], write_size], queue=queue_name)

    print "Finished populating %s" % queue_name


# a multiprocess implementation of the queue population with read tasks
def populate_read(lots_of_args):
    p = Process(target=populate_queue_read, args=lots_of_args)
    p.start()
    return p


# a multiprocess implementation of the queue population with write tasks
def populate_write(lots_of_args):
    p = Process(target=populate_queue_write, args=lots_of_args)
    p.start()
    return p


# a multiprocess implementation of the queue population with update tasks
def populate_update(lots_of_args):
    p = Process(target=populate_queue_update, args=lots_of_args)
    p.start()
    return p


def get_nosql_handler(nosql, ips):
    global NoSQLHandler
    if nosql == 'cassandra':
        from nosql_handlers.cassandra_handler import CassandraHandler as NoSQLHandler
    elif nosql == 'mongodb':
        from nosql_handlers.mongodb_handler import MongoDBHandler as NoSQLHandler
    elif nosql == 'riak':
        from nosql_handlers.riak_handler import RiakHandler as NoSQLHandler
    elif nosql == 'redis':
        from nosql_handlers.redis_handler import RedisHandler as NoSQLHandler
    elif nosql == 'bigcouchdb':
        from nosql_handlers.bigcouch_handler import BigCouchHandler as NoSQLHandler
    elif nosql == 'hbase':
        from nosql_handlers.hbase_handler import HBaseHandler as NoSQLHandler

    return NoSQLHandler(ips)
