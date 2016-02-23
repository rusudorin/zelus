from tasks import read_nosql, start_consuming, stop_consuming
from random import randint
from multiprocessing import Process

nb_reads = 10000
global NoSQLHandler


def populate_queue(nosql, ips, queue_name):
    handler = get_nosql_handler(nosql, ips)

    generated_timestamp_list = []
    timestamp_list = handler.get_timestamp_list()

    for i in range(0, nb_reads):
        index = randint(0, len(timestamp_list))
        generated_timestamp_list.append(timestamp_list[index-1])

    for i in range(0, len(generated_timestamp_list)):
        read_nosql.apply_async(args=[generated_timestamp_list[i]], queue=queue_name)


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
    elif nosql == 'couchdb':
        from nosql_handlers.couchdb_handler import CouchDBHandler as NoSQLHandler
    elif nosql == 'hbase':
        from nosql_handlers.hbase_handler import HBaseHandler as NoSQLHandler

    return NoSQLHandler(ips)


def populate(lots_of_args):
    p = Process(target=populate_queue, args=lots_of_args)
    p.start()

populate_queue('worker2')
populate_queue('worker3')
populate_queue('worker4')
populate_queue('worker5')
populate_queue('worker6')
