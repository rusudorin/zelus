# will be replaced with knapsack
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

def recursive(total_val, node_val, price):
    if total_val <= 0:
	return 0, []

    result_list = []
    config_list = []
    # try for all node types
    for i in range(0, len(node_val)):

        # get recursive results
	result = recursive(total_val - node_val[i], node_val, price)

        # add to the result_list by adding the current price
	result_list.append(price[i] + result[0])

        # add to the config_list by appending the previous solutions
        new_list = result[1]
	new_list.append(str(node_val[i]))
	config_list.append(new_list)

    # get the smallest price
    price_min = min(result_list)

    # get a list of indexes of configurations that have the smallest price
    index_list = get_indexes(result_list, price_min)

    # get the shortest configuration
    config_min = config_list[index_list[0]]
    for i in range(0, len(index_list)):
	if len(config_min) > len(config_list[index_list[i]]):
	    config_min = config_list[index_list[i]]

    return price_min, config_min

node_val = [213, 470, 744, 1912]
values = [0.13, 0.26, 0.52, 1.04]

recurs = recursive(2290, node_val, values)
print recurs
