import const
import data_gen
import sys
import time
from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
from cassandra.concurrent import execute_concurrent_with_args
from nosql_handler import NoSQLHandler


class CassandraHandler(NoSQLHandler):

    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.cluster = self.connect_cluster(ip_list)
        self.session = self.get_session(self.cluster)

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        insertion = "SELECT * from %s where timestamp='%s';"
        intermed_read = insertion % (const.table_name, timestamp)
        exe_result = self.session.execute(intermed_read)
        self.session.cluster.shutdown()
        return exe_result

    def query_manager_setup(self, obj, cluster):
        """
        basic setup for multiprocessing stress test
        """
        obj.session = self.get_session(cluster)
        obj.session.row_factory = tuple_factory
        obj.prepared = obj.session.prepare('SELECT * FROM benchmark.users WHERE timestamp=?')

    def concurrent_read(self, obj, params):
        """
        performs a concurrent execution with the parameters in params
        """
        return execute_concurrent_with_args(obj.session, obj.prepared, params)

    def concurrent_write(self, obj, params, granularity):
        """
        read
        """
        obj.prepared = obj.session.prepare('INSERT INTO users (timestamp, value) VALUES (?, ?) if not exists')
        new_params = []
        for i in range(0, len(params)):
            gen_string = data_gen.generate_str(granularity)
            timestamp = '%.6f' % time.time()
            new_params.append((timestamp, gen_string, ))
        return execute_concurrent_with_args(obj.session, obj.prepared, new_params)

    def concurrent_update(self, obj, params, granularity):
        """
        read
        """
        obj.prepared = obj.session.prepare('UPDATE users SET value = ? where timestamp = ?')
        new_params = []
        for param in params:
            gen_string = data_gen.generate_str(granularity)
            new_params.append((gen_string, param[0]))
        return execute_concurrent_with_args(obj.session, obj.prepared, new_params)

    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return Cluster(contact_points=ip_list, control_connection_timeout=5.0)

    def perform_write(self, granularity):
        """
        create e random string and write it
        """
        insertion = "INSERT INTO %s (timestamp, value) VALUES ('%s', '%s') if not exists;"
        gen_string = data_gen.generate_str(granularity)

        timestamp = time.time()
        intermed_insert = insertion % (const.table_name, '%.6f' % timestamp, gen_string)
        return self.session.execute(intermed_insert)[0][0]

    def perform_update(self, timestamp, granularity):
        """
        create e random string and write it
        """
        insertion = "UPDATE %s SET value = '%s' WHERE timestamp = '%s';"
        gen_string = data_gen.generate_str(granularity)

        timestamp = time.time()
        intermed_insert = insertion % (const.table_name, gen_string, '%.6f' % timestamp)
        return self.session.execute(intermed_insert)[0][0]

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        timestamp_list = self.session.execute("select timestamp from %s;" % const.table_name)
        timestamp_list = [timestamp[0] for timestamp in timestamp_list]
        return timestamp_list

    def get_session(self, cluster):
        """
        establish a session
        """
        try:
            session = cluster.connect(const.keyspace_name)

            # create the table
            self.create_table(session)
            return session
        except Exception as e:
            print e
            print "Cannot establish connection"
            sys.exit(2)

    def create_table(self, columns=1):
        """
        Creates the table in the current keyspace
        """
        try:
            self.session.execute("Create table %s (timestamp text, value text, PRIMARY KEY(timestamp));"
                                 % const.table_name)
        except Exception as e:
            pass
