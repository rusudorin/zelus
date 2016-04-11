from zelus.stormtrooper import Stormtrooper
from zelus.rebel import Rebel
import config
import datetime
import json
import os
import time
import matplotlib.pyplot as plt


def ping_all():
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]
        storm_user = config.stormtrooper_ips[i][1]
        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            c = Stormtrooper(storm_user, storm_ip, i, j)
            c.ping()

    for ip in config.nosql_ips:
        r = Rebel(ip)
        r.ping()


def start_all_consumers():
    for ip in config.nosql_ips:
        r = Rebel(ip)
        r.start_monitoring()

    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]
        storm_user = config.stormtrooper_ips[i][1]
        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            c = Stormtrooper(storm_user, storm_ip, i, j)
            c.start_consuming()


def stop_all_consumers():
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]
        storm_user = config.stormtrooper_ips[i][1]
        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            c = Stormtrooper(storm_user, storm_ip, i, j)
            c.stop_consuming()

    for ip in config.nosql_ips:
        r = Rebel(ip)
        r.stop_monitoring()


def gather_all_reports():
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]
        storm_user = config.stormtrooper_ips[i][1]
        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            c = Stormtrooper(storm_user, storm_ip, i, j)
            c.gather_report()

    for ip in config.nosql_ips:
        r = Rebel(ip)
        r.gather_report()


def clear_all_reports():
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]
        storm_user = config.stormtrooper_ips[i][1]
        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            c = Stormtrooper(storm_user, storm_ip, i, j)
            c.clear_report()

    for ip in config.nosql_ips:
        r = Rebel(ip)
        r.clear_report()


def show_report():
    median_amount = 1000
    today = datetime.datetime.now()

    # iterate in all files
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]

        for j in range(0, config.stormtrooper_numbers[storm_ip]):

            # in case there is one missing, skip
            if not os.path.isfile("report_stormtrooper{0}_{1}.out".format(i, j)):
                continue

            # if there is a json dump created, then skip this stormtrooper
            if os.path.isfile("report_stormtrooper{0}_{1}.json".format(i, j)):
                continue

            # otherwise parse the file and create a dictionary which will be dumped in a new file
            timestamp_list = []
            with open("report_stormtrooper{0}_{1}.out".format(i, j)) as f:
                # iterate in all lines
                for line in f:
                    line_split = line.split(' ')

                    # there might be lines which are defective
                    if len(line_split) != 2:
                        continue

                    timestamp, result = line_split
                    try:
                        dt = datetime.datetime.strptime(timestamp, '%Y-%m-%d:%H:%M:%S,%f')

                        # for simplicity the timestamp has only hours, minutes and seconds
                        dt = dt.replace(year=today.year, month=today.month, day=today.day)

                        # get the epoch time and add the microseconds
                        epoch = time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0

                        timestamp_list.append([epoch, float(result.strip())])
                        # timestamp_dict[epoch] = float(result.strip())
                    except Exception as e:
                        print e
                        pass

            # dump the dictionary in a new file
            with open("report_stormtrooper{0}_{1}.json".format(i, j), 'w') as f:
                f.write(json.dumps(timestamp_list))

    # iterate through all json dumps again and plot the graphs
    plt.figure(1)
    timestamp_dict = {}
    for i in range(0, len(config.stormtrooper_ips)):
        storm_ip = config.stormtrooper_ips[i][0]

        for j in range(0, config.stormtrooper_numbers[storm_ip]):
            with open("report_stormtrooper{0}_{1}.json".format(i, j)) as f:
                plm = f.read()
                temp_list = json.loads(plm)

                for key, value in temp_list:
                    while key in timestamp_dict:
                        key += 0.000001

                    timestamp_dict[key] = value

                list_1 = [x[0] for x in temp_list]
                list_1 = [key - list_1[0] for key in list_1]
                list_1 = get_median_list(list_1, median_amount)

                list_2 = [x[1] for x in temp_list]
                list_2 = [key for key in list_2]
                list_2 = get_median_list(list_2, median_amount)

                plt.plot(list_1, list_2, linestyle="-", linewidth=2.0, marker=None,
                         label='Stormtrooper{0}_{1}'.format(i, j))
    plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)

    # get all timestamps from the dictionary
    timestamp_list = [key for key in timestamp_dict]

    # sort them
    timestamp_list.sort()

    # get the sampled list
    timestamp_median_list = get_median_list(timestamp_list, median_amount)

    # remove the smallest timestamp from all others. This is to ensure it starts from 0
    timestamp_median_list = [key - timestamp_median_list[0] for key in timestamp_median_list]

    # get all the results from the dictionary, based on the sorted timestamp list
    result_list = [timestamp_dict[timestamp] for timestamp in timestamp_list]

    # get the sampled list
    result_median_list = get_median_list(result_list, median_amount)

    # make 3 subplots
    plt.figure(2)
    plt.subplot(4, 1, 1)

    # plot the response times
    plt.plot(timestamp_median_list, result_median_list, linestyle="-",
             linewidth=2.0, marker=None, label='NoSQL response time')

    max_timestamp = max(timestamp_median_list)
    max_result = max(result_median_list)

    plt.axis((0, max_timestamp, 0, max_result))
    plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)

    plt.ylabel('Execution time [s]')

    for ip in config.nosql_ips:

        usage_list = []
        memory_list = []
        # in case there is one missing, skip
        if not os.path.isfile("cpu_usage_nosql{0}.out".format(ip)):
            continue

        with open("cpu_usage_nosql{0}.out".format(ip)) as f:
            # iterate in all lines
            for line in f:
                line_split = line.split(' ')
                usage = line_split[-4]  # cpu usage is the fourth in vmstat
                memory = line_split[4]

                usage_list.append(float(usage))
                memory_list.append(float(memory))

        max_len = len(usage_list)
        plt.subplot(4, 1, 2)
        plt.plot(range(0, max_len), usage_list[0: max_len], linestyle=':', label='CPU Usage {0}'.format(ip))
        axes = plt.gca()
        axes.set_xlim([0, max_timestamp])
        axes.set_ylim([0, max(usage_list)])

        plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)
        plt.ylabel('Usage [%]')

        max_len = len(memory_list)
        plt.subplot(4, 1, 3)
        plt.plot(range(0, max_len), memory_list[0: max_len], linestyle=':', label='Free memory {0}'.format(ip))
        axes = plt.gca()
        axes.set_xlim([0, max_timestamp])
        axes.set_ylim([0, max(memory_list)])

        plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)
        plt.ylabel('Memory [KB]')

    for ip in config.nosql_ips:

        load_list = []
        # in case there is one missing, skip
        if not os.path.isfile("cpu_load_nosql{0}.out".format(ip)):
            continue

        with open("cpu_load_nosql{0}.out".format(ip)) as f:
            # iterate in all lines
            for line in f:
                line_split = line.split('load average:')
                line_split = line_split[1].split(',')  # get only everything after load average
                load = line_split[0]

                load_list.append(float(load))

        max_len = len(load_list)
        plt.subplot(4, 1, 4)
        plt.plot(range(0, max_len), load_list[0: max_len], linestyle='--', label='CPU Load {0}'.format(ip))
        axes = plt.gca()
        axes.set_xlim([0, max_timestamp])

    plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)
    plt.xlabel('Run time [s]')
    plt.ylabel('Load')

    plt.show()


def get_sublist(split_list, amount):
    return [split_list[i:i+amount] for i in range(0, len(split_list), amount)]


def get_median_list(results, amount):

    median_list = []
    for sublist in get_sublist(results, amount):
        median_list.append(sum(sublist)/len(sublist))

    return median_list
