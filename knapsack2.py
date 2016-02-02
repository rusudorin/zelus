# proposes a number of ec2 configurations with the lowest price
import json

def get_indexes(in_list, in_value):
    """
    retrieves a list of indexes at which the value was found
    """
    out_list = []
    for i in range(0, len(in_list)):
	if in_list[i] == in_value:
	    out_list.append(i)

    return out_list

def knapsack(freq, node_freq, price):
    if freq <= 0:
	return 0, []

    result_list = []
    config_list = []
    for i in range(0, len(node_freq)):
	result = knapsack(freq - node_freq[i], node_freq, price)
	result_list.append(price[i] + result[0])
        new_list = result[1]
	new_list.append(str(node_freq[i]))
	config_list.append(new_list)


    price_min = min(result_list)
    index_list = get_indexes(result_list, price_min)

    config_min = config_list[index_list[0]]
    for i in range(0, len(index_list)):
	if len(config_min) > len(config_list[index_list[i]]):
	    config_min = config_list[index_list[i]]
    # print '------------'
    # print result_list
    # print config_list
    # print price_min
    # print config_min
    return price_min, config_min, 1.3

node_freq = [213, 470, 744, 1912]
price = [0.13, 0.26, 0.52, 1.04]

knap = knapsack(2290, node_freq, price)
print knap
