# User IP - the Ip of the machine which will initiate the test
user_ip = '8.8.8.8'

# concurrency lever
concurrency = 4

# RabbitMq IP aka emperor
emperor_ip = "10.141.0.154"

# RabbitMq user
rabbit_user = "jimmy"

# RabbitMq password
rabbit_pass = "kimmel"

# RabbitMq vhost
rabbit_vhost = "live"

# NoSQL Ip list (comma separated, eg a.a.a.a, b.b.b.b)
nosql_ips = ["8.8.8.8"]

# mongo primary ip
mongo_primary_ip = '8.8.8.8'

# mongo secondary ips
mongo_secondary_ips = []

# redis ips
redis_ips = []

# consumers ips
consumer_ips = []

# will contain an ip and the number of workers for that ip
# ex: {"8.8.8.8": 1, "1.1.1.1": 4}
worker_numbers = {}

# will contain a dictionary that will split the consumer_ips to different emperors
# ex: {'8.8.8.8': consumer_ips[:4], '1.1.1.1': consumer_ips[5:]}
# please use list splitting as the ip order is important
worker_emperors = {}

# cassandra ips
cassandra_ips = []

# hbase ips
hbase_ips = []
