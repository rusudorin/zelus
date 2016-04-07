from celery import Celery
from nosql_handlers.mongodb_handler import MongoDBHandler
import config

app = Celery('tasks', broker="amqp://%s:%s@%s/%s" %
                             (config.rabbit_user, config.rabbit_pass, config.emperor_ip, config.rabbit_vhost))
nosql = MongoDBHandler([config.mongo_primary_ip])


@app.task
def read_nosql(x):
    nosql.get_element_by_timestamp(x)
    return 0


@app.task
def write_nosql(x):
    nosql.perform_write(x)
    return 0


@app.task
def update_nosql(x, y):
    nosql.perform_update(x, y)
    return 0
