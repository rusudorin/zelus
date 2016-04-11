from random import randint
from multiprocessing import Process
from numpy.random import choice
import config
import celery


class ReadTask(celery.Task):
    name = 'tasks.read_nosql'


class WriteTask(celery.Task):
    name = 'tasks.write_nosql'


class UpdateTask(celery.Task):
    name = 'tasks.update_nosql'


# populate a queue with read tasks
def populate_queue_read(nosql, stormtrooper_id, worker_id, amount):
    # set the queue name
    queue_name = "worker%d_%d" % (stormtrooper_id, worker_id)

    print "Populating %s..." % queue_name

    # get the corresponding nosql handler
    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    # get all the unique timestamps (ids)
    timestamp_list = handler.get_timestamp_list()

    if len(timestamp_list) == 0:
        print "NoSQL is empty"
        return

    # get random timestamps from the timestamp list
    generated_timestamp_list = []
    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)
        generated_timestamp_list.append(timestamp_list[index-1])

    # get the consumer_ip
    node_ip = config.stormtrooper_ips[stormtrooper_id]
    emperor_ip = get_emperor_ip(node_ip)

    read_nosql = ReadTask()
    app = celery.Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                                        (config.rabbit_user, config.rabbit_pass, emperor_ip, config.rabbit_vhost))
    read_nosql.bind(app)

    for i in range(0, len(generated_timestamp_list)):
        read_nosql.apply_async(args=[generated_timestamp_list[i]], queue=queue_name)
    print "Finished populating %s" % queue_name


# populate a queue with write tasks
def populate_queue_write(stormtrooper_id, worker_id, amount, granularity):
    queue_name = "worker%d_%d" % (stormtrooper_id, worker_id)
    print "Populating %s..." % queue_name

    node_ip = config.stormtrooper_ips[stormtrooper_id]
    emperor_ip = get_emperor_ip(node_ip)

    write_nosql = WriteTask()
    app = celery.Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                                        (config.rabbit_user, config.rabbit_pass, emperor_ip, config.rabbit_vhost))
    write_nosql.bind(app)

    for i in range(0, amount):
        write_nosql.apply_async(args=[granularity], queue=queue_name)

    print "Finished populating %s" % queue_name


# populate a queue with write tasks
def populate_queue_mix(nosql, stormtrooper_id, worker_id, amount, granularity, percent):
    queue_name = "worker%d_%d" % (stormtrooper_id, worker_id)
    print "Populating %s..." % queue_name

    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    generated_timestamp_list = []
    timestamp_list = handler.get_timestamp_list()
    elements = ['read', 'write']

    node_ip = config.stormtrooper_ips[stormtrooper_id]
    emperor_ip = get_emperor_ip(node_ip)

    write_nosql = WriteTask()
    read_nosql = ReadTask()
    app = celery.Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                                        (config.rabbit_user, config.rabbit_pass, emperor_ip, config.rabbit_vhost))
    write_nosql.bind(app)
    read_nosql.bind(app)

    for i in range(0, amount):
        ch = choice(elements, p=[percent, 1-percent])
        if ch == 'read':
            index = randint(0, len(timestamp_list) - 1)
            read_nosql.apply_async(args=[generated_timestamp_list[index]], queue=queue_name)
        else:
            write_nosql.apply_async(args=[granularity], queue=queue_name)

    print "Finished populating %s" % queue_name


# populate a queue with update tasks
def populate_queue_update(nosql, stormtrooper_id, worker_id, amount, granularity, varying=False):
    queue_name = "worker%d_%d" % (stormtrooper_id, worker_id)
    print "Populating %s..." % queue_name
    handler = get_nosql_handler(nosql, [config.mongo_primary_ip])

    timestamp_list = handler.get_timestamp_list()

    node_ip = config.stormtrooper_ips[stormtrooper_id]
    emperor_ip = get_emperor_ip(node_ip)

    update_nosql = UpdateTask()
    app = celery.Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                                        (config.rabbit_user, config.rabbit_pass, emperor_ip, config.rabbit_vhost))
    update_nosql.bind(app)

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)

        if varying:
            write_size = randint(0, granularity)
        else:
            write_size = granularity

        update_nosql.apply_async(args=[timestamp_list[index], write_size], queue=queue_name)

    print "Finished populating %s" % queue_name


def get_emperor_ip(node_ip):

    for key in config.stormtrooper_emperors:
        if node_ip in config.stormtrooper_emperors[key]:
            return key


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

    return NoSQLHandler(ips)
