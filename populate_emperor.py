from random import randint
from multiprocessing import Process
from numpy.random import choice
import celery
import config


class ReadTask(celery.Task):
    name = 'tasks.read_nosql'


class WriteTask(celery.Task):
    name = 'tasks.write_nosql'


class UpdateTask(celery.Task):
    name = 'tasks.update_nosql'


# populate a queue with read tasks
def populate_queue_read(nosql, stormtrooper, amount):
    print "Populating {0}...".format(stormtrooper.queue_name)

    # get the corresponding nosql handler
    nosql_list = [x for x in config.nosql_ips]
    handler = get_nosql_handler(nosql, nosql_list)

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

    read_nosql = ReadTask()
    app = get_celery(stormtrooper.emperor_ip)
    read_nosql.bind(app)

    for i in range(0, len(generated_timestamp_list)):
        read_nosql.apply_async(args=[generated_timestamp_list[i]], queue=stormtrooper.queue_name)
    print "Finished populating {0}".format(stormtrooper.queue_name)


# populate a queue with write tasks
def populate_queue_write(stormtrooper, amount, granularity):
    print "Populating {0}...".format(stormtrooper.queue_name)

    write_nosql = WriteTask()
    app = get_celery(stormtrooper.emperor_ip)
    write_nosql.bind(app)

    for i in range(0, amount):
        write_nosql.apply_async(args=[granularity], queue=stormtrooper.queue_name)

    print "Finished populating {0}".format(stormtrooper.queue_name)


# populate a queue with write tasks
def populate_queue_mix(nosql, stormtrooper, percent, amount, granularity):
    print "Populating {0}...".format(stormtrooper.queue_name)

    # get the corresponding nosql handler
    nosql_list = [x for x in config.nosql_ips]
    handler = get_nosql_handler(nosql, nosql_list)

    timestamp_list = handler.get_timestamp_list()
    elements = ['read', 'write']

    write_nosql = WriteTask()
    read_nosql = ReadTask()
    app = get_celery(stormtrooper.emperor_ip)
    write_nosql.bind(app)
    read_nosql.bind(app)

    for i in range(0, amount):
        ch = choice(elements, p=[percent, 1-percent])
        if ch == 'read':
            index = randint(0, len(timestamp_list) - 1)
            read_nosql.apply_async(args=[timestamp_list[index]], queue=stormtrooper.queue_name)
        else:
            write_nosql.apply_async(args=[granularity], queue=stormtrooper.queue_name)

    print "Finished populating {0}".format(stormtrooper.queue_name)


# populate a queue with update tasks
def populate_queue_update(nosql, stormtrooper, amount, granularity):
    print "Populating {0}...".format(stormtrooper.queue_name)

    # get the corresponding nosql handler
    nosql_list = [x for x in config.nosql_ips]
    handler = get_nosql_handler(nosql, nosql_list)

    timestamp_list = handler.get_timestamp_list()

    update_nosql = UpdateTask()
    app = get_celery(stormtrooper.emperor_ip)
    update_nosql.bind(app)

    for i in range(0, amount):
        index = randint(0, len(timestamp_list) - 1)

        update_nosql.apply_async(args=[timestamp_list[index], granularity], queue=stormtrooper.queue_name)

    print "Finished populating {0}".format(stormtrooper.queue_name)


def get_celery(emperor_ip):
    app = celery.Celery('tasks', broker="amqp://{0}:{1}@{2}/{3}".
                        format(config.rabbit_user, config.rabbit_pass, emperor_ip, config.rabbit_vhost))
    return app


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


# a multiprocess implementation of the queue population with mixed tasks
def populate_mix(lots_of_args):
    p = Process(target=populate_queue_mix, args=lots_of_args)
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
