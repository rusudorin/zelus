from redis import StrictRedis
import const
import time
import data_gen
from nosql_handler import NoSQLHandler


class RedisHandler(NoSQLHandler):

    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.cluster = self.connect_cluster(ip_list)
        self.session = self.get_session(self.cluster)

    def create_table(self, columns=1):
        pass

    def get_session(self, cluster):
        """
        establish a session
        """
        # return cluster[const.keyspace_name][const.table_name]
        return cluster

    def connect_cluster(self, ip_list):
        """
        establish a connection with the cluster
        """
        return StrictRedis(host=ip_list[0], port=6379)

    def query_manager_setup(self, obj, cluster):
        """
        basic setup
        """
        obj.session = self.get_session(cluster)

    def perform_update(self, timestamp, granularity):
        """
        create e random string and write it
        """
        gen_string = data_gen.generate_str(granularity)
        return self.session.set(timestamp, gen_string)

    def perform_write(self, granularity):
        """
        Writes a randomly generated  string to mongo
        """

        gen_string = data_gen.generate_str(granularity)
        timestamp = "%.6f" % time.time()
        return self.session.set(timestamp, gen_string)

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return self.session.keys()

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return self.session.get(timestamp)
