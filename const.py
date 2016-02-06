table_name = 'users'
keyspace_name = 'benchmark'
nosql_list = ['cassandra', 'mongodb', 'riak', 'redis', 'couchdb', 'hbase']
nosql_classes = {
        "cassandra": "CassandraHandler",
        "mongodb": "MongoDBHandler",
        "riak": "RiakHandler",
        "redis": "RedisHandler",
        "couchdb": "CouchDBHandler",
        "hbase": "HBaseHandler"
        }
deploy_folder = 'deploy'
