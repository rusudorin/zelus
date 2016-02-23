import xmlrpclib


class Consumer:

    def __init__(self, ip):
        self.ip = ip
        self.proxy = xmlrpclib.ServerProxy("http://%s:2187" % ip)

    def start_consuming(self):
        self.proxy.start_consuming()

    def stop_consuming(self):
        pass

    def ping(self):
        return self.proxy.ping()
