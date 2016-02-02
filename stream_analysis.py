# will start consuming from rabbit and print the ratio it is consuming at
# the tasks themselvs are in tasks.py

import subprocess
import os
import signal
from datetime import datetime
from celery import Celery

app = Celery('tasks', broker='amqp://ndoye:usmanescu@10.141.0.135/asa')
nb_tasks = 0
first = True
timeout = 10

command = 'celery -A tasks worker --loglevel=info -n worker1'
process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
count = 0
desired = 7.0
ratio = 0

try:
    for line in iter(process.stderr.readline, ''):
        if 'tasks.read_test' in line and 'succeeded' in line:
            line_time = line[1:24]
    	    nb_tasks += 1
    	    dt = datetime.strptime(line_time, '%Y-%m-%d %H:%M:%S,%f')
    	    if first:
    	        first_dt = dt
    	        first = False
    	    diff = dt - first_dt
    	    ratio = nb_tasks/(diff.seconds + 1.0)
	if 'tasks.write_test' in line and 'succeeded' in line:
	    print 'write'
    print ratio
    print nb_tasks
    print diff
except KeyboardInterrupt:
    print ratio
    print nb_tasks
    print diff
    os.killpg(process.pid, signal.SIGTERM)
except Exception as e:
    print e
    os.killpg(process.pid, signal.SIGTERM)
