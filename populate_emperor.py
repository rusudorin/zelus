from tasks import read_nosql, write_nosql, update_nosql, start_consuming, stop_consuming
from random import randint
import config

global NoSQLHandler


def populate_queue_read(nosql, queue_name, amount):
    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    generated_timestamp_list = []
    timestamp_list = handler.get_timestamp_list()

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)
        generated_timestamp_list.append(timestamp_list[index-1])

    for i in range(0, len(generated_timestamp_list)):
        read_nosql.apply_async(args=[generated_timestamp_list[i]], queue=queue_name)


def populate_queue_write(queue_name, amount, granularity, varying=False):

    for i in range(0, amount):
        if varying:
            write_size = randint(0, granularity)
        else:
            write_size = granularity

        write_nosql.apply_async(args=[write_size], queue=queue_name)


def populate_queue_update(nosql, queue_name, amount, granularity, varying=False):

    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    timestamp_list = handler.get_timestamp_list()

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)

        if varying:
            write_size = randint(0, granularity)
        else:
            write_size = granularity

        update_nosql.apply_async(args=[timestamp_list[index], write_size], queue=queue_name)


def start_consumer(queue_name):
    start_consuming.apply_async(args=[0], queue=queue_name)


def stop_consumer(queue_name):
    stop_consuming.apply_async(args=[0], queue=queue_name)


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
