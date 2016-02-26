from deploy import *
from consumer_control import *
from populate_emperor import *
from populate_rebels import *
from multiprocessing import Process


def stormtrooper(lots_of_args):
    p = Process(target=deploy_stormtrooper, args=lots_of_args)
    p.start()


def populate_read(lots_of_args):
    p = Process(target=populate_queue_read, args=lots_of_args)
    p.start()


def populate_write(lots_of_args):
    p = Process(target=populate_queue_write, args=lots_of_args)
    p.start()


def populate_update(lots_of_args):
    p = Process(target=populate_queue_update, args=lots_of_args)
    p.start()


# deploy the emperor
deploy_emperor('root', '10.141.0.154')

# deploy the nosql
deploy_mongodb('root', '10.141.0.155', 'benchmark')

# deploy the consumers
for i in range(0, len(config.consumer_ips)):
    stormtrooper(('root', config.consumer_ips[i], 'mongodb', "worker%d" % i, 4, "worker%d" % i))

# populate the nosql datastore
do_populate([config.mongo_primary_ip], 100, 100000, 'benchmark', 1, 'mongodb')

# populate the emperor with actions
for i in range(0, len(config.consumer_ips)):
    populate_write(("worker%d" % i, 10000, 1500))
    populate_read(('mongodb', "worker%d" % i, 10000))
    populate_update(('mongodb', 'worker%d' % i, 10000, 1000))

# check if rpcs are available
ping_all()

# start consuming
start_all_consumers()

# stop consuming
stop_all_consumers()
