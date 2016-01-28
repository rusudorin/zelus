from celery import Celery
from mongodb_handler import MongoDBHandler

app = Celery('tasks', broker='amqp://guest@localhost//')
mongo = MongoDBHandler(['192.168.33.16'])

#@app.task(rate_limit='700/s')
@app.task
def read_test(x):
    print 'read'
    return mongo.get_element_by_timestamp(x)

@app.task
def write_test(x):
    print 'write'
    return mongo.perform_write(x)
