#NOTE THE 8.8.8.8 IPS are just for examples.

# User IP - the Ip of the machine which will initiate the test
user_ip = '8.8.8.8'

# concurrency lever
concurrency = 4

# RabbitMq IP aka emperor
emperor_ips = [
    ["1.1.1.4", 'user'],
    ["1.1.1.5", 'user'],
    ["1.1.1.6", 'user']
]

# RabbitMq user
rabbit_user = "jimmy"

# RabbitMq password
rabbit_pass = "kimmel"

# RabbitMq vhost
rabbit_vhost = "live"

# NoSQL Ip list
# should be a dictionary of type ip: user
nosql_ips = {
    "1.1.1.1": 'user',
    "1.1.1.2": 'user',
    "1.1.1.3": 'user'
}

# stormtrooper ips
# each item will be a list containing the user and the ip
stormtrooper_ips = [
    ["1.1.1.7", 'user'],
    ["1.1.1.8", 'user'],
    ["1.1.1.9", 'user'],
    ["1.1.1.10", 'user'],
    ["1.1.1.11", 'user'],
    ["1.1.1.12", 'user'],
    ["1.1.1.13", 'user'],
    ["1.1.1.14", 'user'],
    ["1.1.1.15", 'user'],
    ["1.1.1.16", 'user'],
    ["1.1.1.17", 'user'],
    ["1.1.1.18", 'user'],
    ["1.1.1.19", 'user'],
    ["1.1.1.20", 'user'],
    ["1.1.1.21", 'user']
]

# will contain an ip and the number of workers for that ip
# ex: {"8.8.8.8": 1, "1.1.1.1": 4}
stormtrooper_numbers = {
    "1.1.1.7": 1,
    "1.1.1.8": 1,
    "1.1.1.9": 1,
    "1.1.1.10": 1,
    "1.1.1.11": 1,
    "1.1.1.12": 1,
    "1.1.1.13": 1,
    "1.1.1.14": 1,
    "1.1.1.15": 1,
    "1.1.1.16": 1,
    "1.1.1.17": 1,
    "1.1.1.18": 1,
    "1.1.1.19": 1,
    "1.1.1.20": 1,
    "1.1.1.21": 1
}

# will contain a dictionary that will split the stormtrooper_ips to different emperors
# please use list splitting as the ip order is important
# ex: {emperor_ip[0][0]: stormtrooper_ips[0:4], emperor_ip[1][0]: stormtrooper_ips[5:9]}
# this would associate the first emperor with the first 5 stormtrooper ips and the second one with the remaining 5
stormtrooper_emperors = {emperor_ip[0][0]: stormtrooper_ips[0:4], emperor_ip[1][0]: stormtrooper_ips[5:9], emperor_ip[2][0]: stormtrooper_ips[10:14]}

# note: the next configurations are used for automatic clustering which is experimental as of now

# riak ip list
riak_ips = ["8.8.8.8"]

# mongo primary ip
mongo_primary_ip = '8.8.8.8'

# mongo secondary ips
mongo_secondary_ips = ["8.8.8.8"]

# redis ips
redis_ips = ["8.8.8.8"]

# cassandra ips
cassandra_ips = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]

# hbase ips
hbase_ips = ["8.8.8.8"]
