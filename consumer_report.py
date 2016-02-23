from SimpleXMLRPCServer import SimpleXMLRPCServer

consumer_dict = {}


def report(unique_id, ratio):
    # print unique_id + " is consuming with " + str(ratio)
    consumer_dict[unique_id] = ratio
    print consumer_dict
    return True

server = SimpleXMLRPCServer(("10.148.0.254", 1138))
server.register_function(report, "report")
server.serve_forever()
