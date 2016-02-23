import xmlrpclib
from populate_emperor import start_consumer, stop_consumer


class Consumer:

    def __init__(self, ip, unique_id):
        self.ip = ip
        self.unique_id = unique_id
        self.proxy = xmlrpclib.ServerProxy("http://%s:2187" % ip)

    def start_consuming(self):
        self.proxy.start_consuming()
        start_consumer(self.unique_id)

    def stop_consuming(self):
        self.proxy.stop_consuming()
        stop_consumer(self.unique_id)

    def ping(self):
        return self.proxy.ping()
