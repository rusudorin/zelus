from SimpleXMLRPCServer import SimpleXMLRPCServer
import config
import json

ratio_dict = {}
available_dict = {}


def report_ratio(unique_id, ratio):
    ratio_dict[unique_id] = ratio
    print json.dumps(ratio_dict, indent=4)
    return True


def report_ping(unique_id):
    available_dict[unique_id] = True
    print available_dict
    return True


def report_pong(unique_id):
    available_dict[unique_id] = False
    print available_dict
    return True

server = SimpleXMLRPCServer((config.user_ip, 1138))
server.register_function(report_ratio, "report_ratio")
server.register_function(report_ping, "report_ping")
server.register_function(report_pong, "report_pong")
server.serve_forever()
