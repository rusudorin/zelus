from riak import RiakClient
import const
import time
import data_gen
from nosql_handler import NoSQLHandler

class RiakHandler(NoSQLHandler):

    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.cluster = self.connect_cluster(ip_list)
        self.session = self.get_session(self.cluster)

    def create_table(self, columns=1):
        pass

    def get_session(self, cluster):
        """
        generates a random int between lo and hi with an uniform distribution
        """
        return cluster.bucket(const.keyspace_name)

    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return RiakClient(nodes=[{'host': ip_list[0], 'http_port': 8098}])

    def query_manager_setup(self, obj, cluster):
        """
        basic setup for multiprocessing stress test
        """
        obj.session = self.get_session(cluster)

    def perform_write(self, granularity):
        """
        Writes a randomly generated  string to mongo
        """

        gen_string = data_gen.generate_str(granularity)

        timestamp = time.time()
        inserted_id = self.session.new("%.6f" % timestamp, data=gen_string).store().key
        return inserted_id

    def perform_update(self, timestamp, granularity):
        """
        update
        """
        current_element = self.get_element_by_timestamp(timestamp)
        gen_string = data_gen.generate_str(granularity)
        current_element.data = gen_string
        current_element.store()
        return

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return self.session.get_keys()

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return self.session.get(timestamp[0])
