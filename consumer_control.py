import xmlrpclib
from populate_emperor import start_consumer, stop_consumer
import config


class Consumer:

    def __init__(self, ip, unique_id):
        self.ip = ip
        self.unique_id = unique_id
        self.proxy = xmlrpclib.ServerProxy("http://%s:2187" % ip)

    def start_consuming(self):
        response = self.proxy.start_consuming()
        start_consumer(self.unique_id)
        return response

    def stop_consuming(self):
        response = self.proxy.stop_consuming()
        stop_consumer(self.unique_id)
        return response

    def ping(self):
        return self.proxy.ping()


def ping_all():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer(config.consumer_ips[i], "worker%d" % i)
        print "%s responds: %s" % (c.unique_id, c.ping())


def start_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer(config.consumer_ips[i], "worker%d" % i)
        print "%s responds: %s" % (c.unique_id, c.start_consuming())


def stop_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        c = Consumer(config.consumer_ips[i], "worker%d" % i)
        print "%s responds: %s" % (c.unique_id, c.stop_consuming())
