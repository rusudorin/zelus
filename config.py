# User IP - the Ip of the machine which will initiate the test
user_ip = '8.8.8.8'

# concurrency lever
concurrency = 4

# RabbitMq IP aka emperor
emperor_ips = [
    ["1.1.1.1", 'user'],
    ["1.1.1.2", 'user']
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
    "2.2.2.1": 'user',
    "2.2.2.2": 'user'
}

# stormtrooper ips
# each item will be a list containing the user and the ip
stormtrooper_ips = [
    ["3.3.3.1", 'user'],
    ["3.3.3.2", 'user']
]

# will contain an ip and the number of workers for that ip
# ex: {"8.8.8.8": 1, "1.1.1.1": 4}
stormtrooper_numbers = {}

# will contain a dictionary that will split the stormtrooper_ips to different emperors
# please use list splitting as the ip order is important
# ex: {emperor_ip[0][0]: stormtrooper_ips[0:4], emperor_ip[1][0]: stormtrooper_ips[5:10]}
# this would associate the first emperor with the first 5 stormtrooper ips and the second one with the remaining 5
stormtrooper_emperors = {}

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
cassandra_ips = ["8.8.8.8"]

# hbase ips
hbase_ips = ["8.8.8.8"]
