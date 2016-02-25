# will perform a read or write to a certain nosql
from celery import Celery
from data_gen import generate_str
from nosql_handlers.mongodb_handler import MongoDBHandler
import config

app = Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                             (config.rabbit_user, config.rabbit_pass, config.emperor_ip, config.rabbit_vhost))
nosql = MongoDBHandler([config.mongo_primary_ip])


@app.task
def read_nosql(x):
    return nosql.get_element_by_timestamp(x)


@app.task
def write_nosql(x):
    return nosql.perform_write(generate_str(x))


@app.task
def update_nosql(x, y):
    return nosql.perform_update(x, generate_str(y))


@app.task
def start_consuming(x):
    return True


@app.task
def stop_consuming(x):
    return True
