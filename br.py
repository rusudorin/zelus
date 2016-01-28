# broadcast to a certain Celery worker which rate to use

from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

app.control.broadcast('rate_limit', arguments={'task_name': 'tasks.add', 'rate_limit': '40/s'})

