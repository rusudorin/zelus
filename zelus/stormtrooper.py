from celery import Celery
import config
import os
import subprocess


class Stormtrooper:

    def __init__(self, user, ip, unique_id, worker_number):
        self.user = user
        self.ip = ip
        self.unique_id = unique_id
        self.worker_number = worker_number

    @property
    def emperor_ip(self):
        for key in config.stormtrooper_emperors:
            if self.ip in config.stormtrooper_emperors[key]:
                return key

    @property
    def queue_name(self):
        return "stormtrooper{0}_{1}".format(self.unique_id, self.worker_number)

    def start_consuming(self, rate=None, task=None):
        print "Starting stormtrooper{0}_{1}...".format(self.unique_id, self.worker_number)

        os.system("ssh {0}@{1} 'supervisorctl start stream_analysis{2}_{3}'".format(self.user, self.ip,
                                                                                    self.unique_id,
                                                                                    self.worker_number))
        if rate is not None and task is not None:
            app = Celery('tasks', broker="amqp://{0}:{1}@{2}/{3}".format(config.rabbit_user,
                                                                         config.rabbit_pass,
                                                                         self.emperor_ip,
                                                                         config.rabbit_vhost))

            app.control.broadcast('rate_limit', arguments={'task_name': task, 'rate_limit': '{0}/s'.format(rate)})

    def stop_consuming(self):
        print "Stopping stormtrooper{0}_{1}...".format(self.unique_id, self.worker_number)

        os.system("ssh {0}@{1} 'supervisorctl stop stream_analysis{2}_{3}'".format(self.user, self.ip, self.unique_id,
                                                                                   self.worker_number))

        subprocess.Popen(['ssh', "{0}@{1}".format(self.user, self.ip),
                          "ps auwx | grep 'celery' | grep 'worker' | awk '{print $2}' | xargs kill -9"],
                         stdout=subprocess.PIPE)  # if it looks hacky, thank the official celery page. They provided it

    def ping(self):
        print "\nPinging stormtrooper{0}_{1}...".format(self.unique_id, self.worker_number)
        os.system("ssh {0}@{1} 'supervisorctl status stream_analysis{2}_{3}'".format(self.user, self.ip, self.unique_id,
                                                                                     self.worker_number))

    def gather_report(self):
        print "Gathering report from stormtrooper{0}_{1}".format(self.unique_id, self.worker_number)
        os.system("scp {0}@{1}:/var/log/supervisor/stream_analysis{2}_{3}.out report_worker{2}_{3}.out".
                  format(self.user, self.ip, self.unique_id, self.worker_number))

    def clear_report(self):
        print "Clearing report from stormtrooper{0}_{1}".format(self.unique_id, self.worker_number)
        os.system("ssh {0}@{1} 'rm /var/log/supervisor/stream_analysis{2}_{3}.out'".
                  format(self.user, self.ip, self.unique_id, self.worker_number))
        os.system("ssh {0}@{1} 'rm /var/log/supervisor/stream_analysis{2}_{3}.err'".
                  format(self.user, self.ip, self.unique_id, self.worker_number))
