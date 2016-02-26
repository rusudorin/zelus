from pymongo import MongoClient
import subprocess
import const
import time
import data_gen
from nosql_handler import NoSQLHandler


class MongoDBHandler(NoSQLHandler):

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
        return cluster[const.keyspace_name][const.table_name]

    def connect_cluster(self, ip_list):
        """
        establish a connection with the cluster
        """
        return MongoClient(ip_list[0], 27017)

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
        update_dict = {'_id': timestamp, 'value': gen_string}
        return self.session.update({'_id': update_dict['_id']}, update_dict)

    def perform_write(self, granularity):
        """
        Writes a randomly generated  string to mongo
        """

        gen_string = data_gen.generate_str(granularity)

        timestamp = time.time()
        insert_dict = {'_id': timestamp, 'value': gen_string}
        try:
            inserted_id = self.session.insert_one(insert_dict).inserted_id
        except Exception as e:
            print e
            inserted_id = False
        return inserted_id

    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return [doc_object['_id'] for doc_object in self.session.find()]

    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return self.session.find_one({'_id': timestamp})
