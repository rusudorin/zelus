# work in progress
# should do stress tests and gather data

from stress_test_read import do_stress_test
from populate import do_populate
from operator import itemgetter
from multiprocess_cassandra import do_stress_read
import time

# do_populate(['192.168.7.10'], 100, 100000, 'benchmark', 1, 'hbase')
# do_populate(['192.168.33.15'], 100, 100000, 'benchmark', 1, 'mongodb')


# cassandra_list = do_stress_read('cassandra', ['192.168.33.11'], 'generate_random', 10000, 1)
# time.sleep(2)
# mongodb_list = do_stress_read('hbase', ['192.168.7.10'], 'generate_random', 10000, 1)

# sorted(cassandra_list, key=itemgetter(1))
# sorted(mongodb_list, key=itemgetter(1))

# mongo_vals = [obj[1] for obj in mongodb_list]
# mongo_times = [obj[0] for obj in mongodb_list]

# cass_vals = [obj[1] for obj in cassandra_list]
# cass_times = [obj[0] for obj in cassandra_list]

# mongo_init = mongo_times[0]
# mongo_times = [obj - mongo_init for obj in mongo_times]

# cass_init = cass_times[0]
# cass_times = [obj - cass_init for obj in cass_times]

# print len(mongodb_list)
# print len(cassandra_list)
# from matplotlib import pyplot

# pyplot.plot(range(1, len(mongo_vals) + 1), mongo_vals, label='hbase')
# pyplot.plot(range(1, len(cass_vals) + 1), cass_vals, label='Cassandra')
# pyplot.legend(framealpha=0.5)
# pyplot.show()
# import pdb;pdb.set_trace()

from redis_handler import RedisHandler
from stress_test import StressTest

cass = RedisHandler(['192.168.33.16'])
# cass.populate(10, 10000)
ste = StressTest(cass, 4, 3, 100)
# print cass.get_timestamp_list()
# print ste.do_stress_write(1000)
# print ste.do_stress_read('generate_random', 1000)
print ste.do_stress_update('generate_random', 1000)
