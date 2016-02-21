from pymongo import MongoClient
import argparse
import sys
import subprocess
import const
import time

def create_parser():
    """
    creates the parser from the arguments specified
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--ip_list", type=str, nargs="+", help="The list of IPs of the cluster")
    parser.add_argument("--granularity", type=int, help="The granularity of the items to be added")
    parser.add_argument("--size", type=int, help="The total size in bytes")
    parser.add_argument("--keyspace", type=str, help="The keyspace that will be created")
    parser.add_argument("--columns", type=int, default=1, help="The number of columns... not done yet")
    parser.add_argument("--nosql", type=str, help="The NoSQL which will be used")

    return parser

def parse_arguments(arguments, parser):
    """
    get arguments
    """
    args = parser.parse_args(arguments)
    return args

def get_rand_string(granularity):
    """
    get a random string
    """

    script_cmd = "python data_gen.py --size %d " % granularity
    return subprocess.check_output(script_cmd, shell=True).strip()

def set_environment(nosql):
    """
    Sets the correct imports according to the chosen nosql datastore
    """
    if nosql == 'cassandra':
        global NoSQLHandler
        from cassandra_handler import CassandraHandler as NoSQLHandler
    elif nosql == 'mongodb':
        global NoSQLHandler
        from mongodb_handler import MongoDBHandler as NoSQLHandler
    elif nosql == 'riak':
        global NoSQLHandler
        from riak_handler import RiakHandler as NoSQLHandler
    elif nosql == 'couchdb':
        global NoSQLHandler
        from couchdb_handler import CouchDBHandler as NoSQLHandler
    elif nosql == 'hbase':
        global NoSQLHandler
        from hbase_handler import HBaseHandler as NoSQLHandler

def main():

    # initiate parser
    parser = create_parser()
    args = parse_arguments(sys.argv[1:], parser)

    # get arguments as variables
    ip_list = args.ip_list
    granularity = args.granularity
    total_size = args.size
    keyspace = args.keyspace
    columns = args.columns
    nosql = args.nosql

    do_populate(ip_list, granularity, total_size, keyspace, columns, nosql)

def do_populate(ip_list, granularity, total_size, keyspace, columns, nosql):
    # basic checks

    if not ip_list:
        print "No ips"
        sys.exit(1)

    if not granularity:
        print "No granularity"
        sys.exit(2)

    if not total_size:
        print "No total_size"
        sys.exit(3)

    if not keyspace:
        print "No keyspace"
        sys.exit(4)

    if columns > total_size:
        print "Cannot have more columns than the total number of bytes"
        sys.exit(5)

    if nosql not in const.nosql_list:
        print "NoSQL datastore not supported"
        sys.exit(5)

    set_environment(nosql)

    # get the session
    nosql = NoSQLHandler(['ip_goes_here'])

    i = 1
    while i * granularity <= total_size:

        # if the item was not added then do not increment the counter
        if nosql.perform_write(granularity):
            i += 1

if __name__ == "__main__":
    main()
