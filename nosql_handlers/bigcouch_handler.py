import couchdbkit
import const
import time
import data_gen
from nosql_handler import NoSQLHandler


class CouchDBHandler(NoSQLHandler):

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
        # try:
        db = cluster.get_or_create_db(const.keyspace_name)
        # except:
        #     db = cluster.database(const.keyspace_name)
        return db

    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return couchdbkit.Server('http://' + ip_list[0] + ":5984")

    def query_manager_setup(self, obj, cluster):
        """
        basic setup for the multiprocessing stress test
        """
        obj.session = self.get_session(cluster)

    def perform_write(self, granularity):
        """
        Writes a randomly generated  string to mongo
        """

        gen_string = data_gen.generate_str(granularity)

        timestamp = time.time()
        insert_dict = {'_id': "%.6f" % timestamp, 'value': gen_string}
        try:
            self.session.save_doc(insert_dict)
            inserted_id = insert_dict['_id']
        except Exception as e:
            inserted_id = False
            print e
        # print inserted_id
        return inserted_id

    def perform_update(self, timestamp, granularity):
        """
        perform update for a single object
        """
        gen_string = data_gen.generate_str(granularity)
        current_doc = self.get_element_by_timestamp(timestamp)
        current_doc['value'] = gen_string
        self.session.save_doc(current_doc)
        return

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return [key['id'] for key in self.session]

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return self.session.get(timestamp)
