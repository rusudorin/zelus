from populate_emperor import start_consumer, stop_consumer
import config
import os


class Consumer:

    def __init__(self, user, ip, unique_id):
        self.user = user
        self.ip = ip
        self.unique_id = unique_id

    def start_consuming(self):
        os.system("ssh %s@%s 'supervisorctl start stream_analysis'" % (self.user, self.ip))
        start_consumer(self.unique_id)

    def stop_consuming(self):
        os.system("ssh %s@%s 'supervisorctl stop stream_analysis'" % (self.user, self.ip))
        os.system("ssh %s@%s 'ps auwx | grep 'celery' | grep 'worker' | awk '{print $2}' | xargs kill -9" %
                  (self.user, self.ip))
        stop_consumer(self.unique_id)

    def ping(self):
        print self.unique_id
        os.system("ssh %s@%s 'supervisorctl status stream_analysis'" % (self.user, self.ip))


def ping_all():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer('root', config.consumer_ips[i], "worker%d" % i)
        c.ping()


def start_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer('root', config.consumer_ips[i], "worker%d" % i)
        c.start_consuming()


def stop_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer('root', config.consumer_ips[i], "worker%d" % i)
        c.stop_consuming()
