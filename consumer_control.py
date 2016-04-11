from celery import Celery
from populate_emperor import get_emperor_ip
import config
import datetime
import json
import os
import time
import matplotlib.pyplot as plt
import subprocess


class Consumer:

    def __init__(self, user, ip, unique_id, worker_number):
        self.user = user
        self.ip = ip
        self.unique_id = unique_id
        self.worker_number = worker_number

    def start_consuming(self, rate=None, task=None):
        os.system("ssh %s@%s 'supervisorctl start stream_analysis%d_%d'" % (self.user, self.ip,
                                                                            self.unique_id,
                                                                            self.worker_number))
        if rate is not None and task is not None:
            app = Celery('tasks', broker="amqp://%s:%s@%s/%s" % (config.rabbit_user,
                                                                 config.rabbit_pass,
                                                                 get_emperor_ip(self.ip),
                                                                 config.rabbit_vhost))

            app.control.broadcast('rate_limit', arguments={'task_name': task, 'rate_limit': '%d/s' % rate})

    def stop_consuming(self):
        os.system("ssh %s@%s 'supervisorctl stop stream_analysis%d_%d'" % (self.user, self.ip, self.unique_id,
                                                                           self.worker_number))

        subprocess.Popen(['ssh', "%s@%s" % (self.user, self.ip),
                          "ps auwx | grep 'celery' | grep 'worker' | awk '{print $2}' | xargs kill -9"],
                         stdout=subprocess.PIPE)  # if it looks hacky, thank the official celery page. They provided it

    def ping(self):
        os.system("ssh %s@%s 'supervisorctl status stream_analysis%d_%d'" % (self.user, self.ip, self.unique_id,
                                                                             self.worker_number))

    def gather_report(self):
        print "Gathering report from worker%d_%d" % (self.unique_id, self.worker_number)
        os.system("scp %s@%s:/var/log/supervisor/stream_analysis%d_%d.out report_worker%d_%d.out" %
                  (self.user, self.ip, self.unique_id, self.worker_number, self.unique_id, self.worker_number))

    def clear_report(self):
        print "Clearing report from worker%d_%d" % (self.unique_id, self.worker_number)
        os.system("ssh %s@%s 'rm /var/log/supervisor/stream_analysis%d_%d.out'" %
                  (self.user, self.ip, self.unique_id, self.worker_number))
        os.system("ssh %s@%s 'rm /var/log/supervisor/stream_analysis%d_%d.err'" %
                  (self.user, self.ip, self.unique_id, self.worker_number))


def ping_all():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "\nPinging worker%d_%d..." % (i, worker)
            c.ping()
    for i in range(0, len(config.nosql_ips)):
        os.system("ssh %s@%s 'supervisorctl status cpu_usage'" % ('root', config.nosql_ips[i]))
        os.system("ssh %s@%s 'supervisorctl status cpu_load'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def start_all_consumers():
    for i in range(0, len(config.nosql_ips)):
        print "Starting nosql %s" % config.nosql_ips[i]
        os.system("ssh %s@%s 'supervisorctl start cpu_usage'" % ('root', config.nosql_ips[i]))
        os.system("ssh %s@%s 'supervisorctl start cpu_load'" % ('root', config.nosql_ips[i]))
        # TODO move users to config

    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "Starting worker%d_%d..." % (i, worker)
            c.start_consuming()


def stop_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "Stopping worker%d_%d..." % (i, worker)
            c.stop_consuming()
    for i in range(0, len(config.nosql_ips)):
        print "Stopping nosql %s" % config.nosql_ips[i]
        os.system("ssh %s@%s 'supervisorctl stop cpu_usage'" % ('root', config.nosql_ips[i]))
        os.system("ssh %s@%s 'supervisorctl stop cpu_load'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def gather_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.gather_report()

    for i in range(0, len(config.nosql_ips)):
        print "Gathering report from %s" % config.nosql_ips[i]
        os.system("scp %s@%s:/var/log/supervisor/cpu_usage.out cpu_usage_nosql%s.out" %
                  ('root', config.nosql_ips[i], config.nosql_ips[i]))
        os.system("scp %s@%s:/var/log/supervisor/cpu_load.out cpu_load_nosql%s.out" %
                  ('root', config.nosql_ips[i], config.nosql_ips[i]))
        # TODO move users to config


def clear_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.clear_report()
    for i in range(0, len(config.nosql_ips)):
        print "Clearing report from %s" % config.nosql_ips[i]
        os.system("ssh %s@%s 'rm /var/log/supervisor/cpu_usage.out'" % ('root', config.nosql_ips[i]))
        os.system("ssh %s@%s 'rm /var/log/supervisor/cpu_load.out'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def show_report():
    median_amount = 1000
    today = datetime.datetime.now()

    # iterate in all files
    for i in range(0, len(config.consumer_ips)):

        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):

            # in case there is one missing, skip
            if not os.path.isfile("report_worker%d_%d.out" % (i, worker)):
                continue

            # if there is a json dump created, then skip this worker
            if os.path.isfile("report_worker%d_%d.json" % (i, worker)):
                continue

            # otherwise parse the file and create a dictionary which will be dumped in a new file
            timestamp_list = []
            with open("report_worker%d_%d.out" % (i, worker)) as f:
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
            with open("report_worker%d_%d.json" % (i, worker), 'w') as f:
                f.write(json.dumps(timestamp_list))

    # iterate through all json dumps again and plot the graphs
    plt.figure(1)
    timestamp_dict = {}
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            with open("report_worker%d_%d.json" % (i, worker)) as f:
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

                plt.plot(list_1, list_2, linestyle="-", linewidth=2.0, marker=None, label='Worker%d_%d' % (i, worker))
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

    for i in range(0, len(config.nosql_ips)):

        usage_list = []
        memory_list = []
        # in case there is one missing, skip
        if not os.path.isfile("cpu_usage_nosql%s.out" % config.nosql_ips[i]):
            continue

        with open("cpu_usage_nosql%s.out" % config.nosql_ips[i]) as f:
            # iterate in all lines
            for line in f:
                line_split = line.split(' ')
                usage = line_split[-4]  # cpu usage is the fourth in vmstat
                memory = line_split[4]

                usage_list.append(float(usage))
                memory_list.append(float(memory))

        max_len = len(usage_list)
        plt.subplot(4, 1, 2)
        plt.plot(range(0, max_len), usage_list[0: max_len], linestyle=':', label='CPU Usage %s' % config.nosql_ips[i])
        axes = plt.gca()
        axes.set_xlim([0, max_timestamp])
        axes.set_ylim([0, max(usage_list)])

        plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)
        plt.ylabel('Usage [%]')

        max_len = len(memory_list)
        plt.subplot(4, 1, 3)
        plt.plot(range(0, max_len), memory_list[0: max_len], linestyle=':', label='Free memory %s'
                                                                                  % config.nosql_ips[i])
        axes = plt.gca()
        axes.set_xlim([0, max_timestamp])
        axes.set_ylim([0, max(memory_list)])

        plt.legend(loc="upper right", ncol=2, shadow=True, title="Legend", fancybox=True)
        plt.ylabel('Memory [KB]')

    for i in range(0, len(config.nosql_ips)):

        load_list = []
        # in case there is one missing, skip
        if not os.path.isfile("cpu_load_nosql%s.out" % config.nosql_ips[i]):
            continue

        with open("cpu_load_nosql%s.out" % config.nosql_ips[i]) as f:
            # iterate in all lines
            for line in f:
                line_split = line.split('load average:')
                line_split = line_split[1].split(',')  # get only everything after load average
                load = line_split[0]

                load_list.append(float(load))

        max_len = len(load_list)
        plt.subplot(4, 1, 4)
        plt.plot(range(0, max_len), load_list[0: max_len], linestyle='--', label='CPU Load %s' % config.nosql_ips[i])
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
