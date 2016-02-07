import xmlrpclib
import config

for ip in config.consumer_ips:
    proxy = xmlrpclib.ServerProxy("http://" + ip + ":2187/")
    proxy.start_consuming()
