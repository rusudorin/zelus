from numpy.random import choice
from tasks import read_test, write_test
from mongodb_handler import MongoDBHandler
from random import randint

mongo = MongoDBHandler(['192.168.33.16'])

elements = ['read', 'write']
weight = [0.9, 0.1]

nb_op = 10000
gran = 100

timestamp_list = mongo.get_timestamp_list()

for i in range(0, nb_op):
    if choice(elements, p=weight) == 'read':
	index = randint(0, len(timestamp_list) - 1)
	read_test.delay(timestamp_list[index])
    else:
	write_test.delay(gran)
