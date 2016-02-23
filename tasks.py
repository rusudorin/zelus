# will perform a read or write to a certain nosql
from celery import Celery
from mongodb_handler import MongoDBHandler
import json
import time
import config

app = Celery('tasks', broker="amqp://%s:%s@%s/%s" % (config.rabbit_user, config.rabbit_pass, config.rabbit_ip, config.rabbit_vhost))
mongo = MongoDBHandler([config.mongo_primary_ip])


@app.task
def read_nosql(x):
    from celery import current_task
    task_id = current_task.request.id
    print 'read ' + task_id + " " +  json.dumps({"time": time.time()})
    return mongo.get_element_by_timestamp(x)


@app.task
def write_nosql(x):
    print 'write'
    return mongo.perform_write(x)


@app.task
def start_consuming(x):
    return True


@app.task
def stop_consuming(x):
    return True
