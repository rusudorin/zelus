import config
import datetime
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

    def start_consuming(self):
        os.system("ssh %s@%s 'supervisorctl start stream_analysis%d_%d'" % (self.user, self.ip, self.unique_id,
                                                                            self.worker_number))

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


def ping_all():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "\nPinging worker%d_%d..." % (i, worker)
            c.ping()
    for i in range(0, len(config.nosql_ips)):
        os.system("ssh %s@%s 'supervisorctl status cpu_usage'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def start_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "Starting worker%d_%d..." % (i, worker)
            c.start_consuming()
    for i in range(0, len(config.nosql_ips)):
        os.system("ssh %s@%s 'supervisorctl start cpu_usage'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def stop_all_consumers():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            print "Stopping worker%d_%d..." % (i, worker)
            c.stop_consuming()
    for i in range(0, len(config.nosql_ips)):
        os.system("ssh %s@%s 'supervisorctl stop cpu_usage'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def gather_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.gather_report()

    for i in range(0, len(config.nosql_ips)):
        os.system("scp %s@%s:/var/log/supervisor/cpu_usage.out cpu_usage_nosql%s.out" %
                  ('root', config.nosql_ips[i], config.nosql_ips[i]))
        # TODO move users to config


def clear_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.clear_report()
    for i in range(0, len(config.nosql_ips)):
        os.system("ssh %s@%s 'rm /var/log/supervisor/cpu_usage.out'" % ('root', config.nosql_ips[i]))
        # TODO move users to config


def show_report():
    median_amount = 1000
    timestamp_dict = {}
    today = datetime.datetime.now()

    # iterate in all files
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):

            # in case there is one missing, skip
            if not os.path.isfile("report_worker%d_%d.out" % (i, worker)):
                continue

            with open("report_worker%d_%d.out" % (i, worker)) as f:
                # iterate in all lines
                for line in f:
                    line_split = line.split(' ')

                    # there might be lines which are defective
                    if len(line_split) != 2:
                        continue

                    timestamp, result = line_split
                    try:
                        dt = datetime.datetime.strptime(timestamp, '%H:%M:%S,%f')

                        # for simplicity the timestamp has only hours, minutes and seconds
                        dt = dt.replace(year=today.year, month=today.month, day=today.day)

                        # if there are identical timestamps, keep adding one microsecond
                        while dt in timestamp_dict:
                            dt = dt.replace(microsecond=dt.microsecond + 1)

                        # get the epoch time and add the microseconds
                        epoch = time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0

                        timestamp_dict[epoch] = float(result.strip())
                    except Exception as e:
                        print e
                        pass

    timestamp_list = [key for key in timestamp_dict]
    timestamp_list.sort()
    timestamp_median_list = get_median_list(timestamp_list, median_amount)
    timestamp_median_list = [key - timestamp_median_list[0] for key in timestamp_median_list]

    result_list = [timestamp_dict[timestamp] for timestamp in timestamp_list]
    result_median_list = get_median_list(result_list, median_amount)

    fig, ax = plt.subplots()
    ax.set_xlim([min(timestamp_median_list), max(timestamp_median_list)])
    ax.set_ylim([0, max(result_median_list)])
    ax.plot(timestamp_median_list, result_median_list, linestyle="-", marker=None)

    plt.show()


def get_sublist(split_list, amount):
    return [split_list[i:i+amount] for i in range(0, len(split_list), amount)]


def get_median_list(results, amount):

    median_list = []
    for sublist in get_sublist(results, amount):
        median_list.append(sum(sublist)/len(sublist))

    return median_list
