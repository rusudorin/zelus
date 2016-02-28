table_name = 'users'
keyspace_name = 'benchmark'
nosql_list = ['cassandra', 'mongodb', 'riak', 'redis', 'bigcouch', 'hbase']
nosql_classes = {
        "cassandra": "CassandraHandler",
        "mongodb": "MongoDBHandler",
        "riak": "RiakHandler",
        "redis": "RedisHandler",
        "bigcouch": "BigCouchHandler",
        "hbase": "HBaseHandler"
        }
deploy_folder = 'deploy'
