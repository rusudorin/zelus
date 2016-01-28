# Populate a certain queue

from tasks import read_test
#from mongodb_handler import MongoDBHandler
from random import randint

nb_reads = 100000
#mongo = MongoDBHandler(['192.168.33.16'])

generated_timestamp_list = []
#timestamp_list = mongo.get_timestamp_list()

for i in range(0, nb_reads):
    index = randint(0, nb_reads)
    generated_timestamp_list.append(index)

for i in range(0, len(generated_timestamp_list)):
    read_test.apply_async(args=[generated_timestamp_list[i]], queue='worker5')
