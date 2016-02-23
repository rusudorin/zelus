import abc


class NoSQLHandler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_session(self, cluster):
        """
        establish a session
        """
        return

    @abc.abstractmethod
    def connect_cluster(self, ip_list):
        """
        establish connection with the cluster
        """
        return

    @abc.abstractmethod
    def query_manager_setup(self, obj, session):
        """
        basic setup for multiprocessing stress test
        """
        return

    def concurrent_read(self, obj, params):
        """
        read
        """
        read_list = []
        for param in params:
            read_list.append(self.get_element_by_timestamp(param))
        return read_list

    def concurrent_write(self, obj, params, granularity):
        """
        read
        """
        read_list = []
        for param in params:
            read_list.append(self.perform_write(granularity))
        return read_list

    def concurrent_update(self, obj, params, granularity):
        """
        read
        """
        read_list = []
        for param in params:
            read_list.append(self.perform_update(param, granularity))
        return read_list

    @abc.abstractmethod
    def create_table(self, columns=1):
        """
        Creates the table in the current keyspace
        """
        return

    @abc.abstractmethod
    def perform_write(self, granularity):
        """
        create e random string and write it
        """
        return

    @abc.abstractmethod
    def perform_update(self, timestamp, granularity):
        """
        create e random string and write it
        """
        return

    @abc.abstractmethod
    def get_timestamp_list(self):
        """
        gets all the items from the table
        """
        return

    @abc.abstractmethod
    def get_element_by_timestamp(self, timestamp):
        """
        retrieves an element using the unique timestamp
        """
        return

    def populate(self, granularity, total_size):
        """
        populate the data base
        :param granularity: the individual granularity of an item
        :param total_size: the overall size
        :return:
        """
        i = 1
        while i * granularity <= total_size:

            # if the item was not added then do not increment the counter
            if self.perform_write(granularity):
                i += 1
