from happybase import Connection
import const
import time
import data_gen
from nosql_handler import NoSQLHandler


class HBaseHandler(NoSQLHandler):

    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.cluster = self.connect_cluster(ip_list)
        self.session = self.get_session(self.cluster)

    def create_table(self, columns=1):
        pass

    def get_session(self, cluster):
        """
        get the session
        """
        return cluster.table(const.table_name)

    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return Connection(host=ip_list[0], port=9090)

    def query_manager_setup(self, obj, cluster):
        """
        basic setup for multiprocessing test
        """
        obj.session = self.get_session(cluster)

    def perform_write(self, granularity):
        """
        Writes a randomly generated  string to mongo
        """

        gen_string = data_gen.generate_str(granularity)

        timestamp = "%.6f" % time.time()
        insert_dict = {'timestamp:col1': timestamp, 'value:col2': gen_string}
        try:
            self.session.put(timestamp, insert_dict)
            inserted_id = True
        except Exception as e:
            print e
            inserted_id = False
        print inserted_id
        return inserted_id

    def perform_update(self, timestamp, granularity):
        """
        update
        """
        gen_string = data_gen.generate_str(granularity)
        insert_dict = {'timestamp:col1': timestamp[0], 'value:col2': gen_string}
        self.session.put(timestamp[0], insert_dict)
        return

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        scan_result = self.session.scan(filter=b'KeyOnlyFilter() AND FirstKeyOnlyFilter()')
        return [doc_object[0] for doc_object in scan_result]

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return self.session.row(timestamp[0])
