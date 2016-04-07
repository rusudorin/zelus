import const
import data_gen
import time
from nosql_handler import NoSQLHandler
import pycassa


class CassandraHandler(NoSQLHandler):

    def __init__(self, ip_list):
        self.ip_list = ip_list
        # create the table if it does not exist yet
        self.create_table()
        self.pool = self.connect_cluster(self.ip_list)
        self.cf = self.get_session(self.pool)

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        try:
            return self.cf.get(timestamp)
        except:
            return False

    def query_manager_setup(self, obj, cluster):
        """
        basic setup for multiprocessing stress test
        """
        pass

    def concurrent_read(self, obj, params):
        """
        performs a concurrent execution with the parameters in params
        """
        pass

    def concurrent_write(self, obj, params, granularity):
        """
        read
        """
        pass

    def concurrent_update(self, obj, params, granularity):
        """
        read
        """
        pass

    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return pycassa.ConnectionPool(const.keyspace_name, server_list=self.ip_list)

    def perform_write(self, granularity):
        """
        create e random string and write it
        """
        gen_string = data_gen.generate_str(granularity)

        timestamp = str(time.time())
        return self.cf.insert(timestamp, {"column": gen_string})

    def perform_update(self, timestamp, granularity):
        """
        create e random string and write it
        """
        gen_string = data_gen.generate_str(granularity)

        return self.cf.insert(timestamp, {"column": gen_string})

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return [x[0] for x in self.cf.get_range()]

    def get_session(self, cluster):
        """
        establish a session
        """
        session = pycassa.ColumnFamily(cluster, const.table_name)

        return session

    def create_table(self, columns=1):
        """
        Creates the table in the current keyspace
        """
        try:
            system_manager = pycassa.system_manager.SystemManager("%s:9160" % self.ip_list[0])
            system_manager.create_keyspace(const.keyspace_name, pycassa.system_manager.SIMPLE_STRATEGY,
                                           {'replication_factor': '1'})
            system_manager.create_column_family(const.keyspace_name, const.table_name)
        except Exception as e:
            print e
            pass
