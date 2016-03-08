import config
import datetime
import os
import matplotlib.pyplot as plt
import subprocess


class Consumer:

    def __init__(self, user, ip, unique_id, worker_number):
        self.user = user
        self.ip = ip
        self.unique_id = unique_id
        self.worker_number = worker_number

    def start_consuming(self):
        os.system("ssh %s@%s 'supervisorctl start stream_analysis%d'" % (self.user, self.ip, self.worker_number))

    def stop_consuming(self):
        os.system("ssh %s@%s 'supervisorctl stop stream_analysis%d'" % (self.user, self.ip, self.worker_number))
        subprocess.Popen(['ssh', "%s@%s" % (self.user, self.ip),
                          "ps auwx | grep 'celery' | grep 'worker' | awk '{print $2}' | xargs kill -9"],
                         stdout=subprocess.PIPE)  # if it looks hacky, thank the official celery page. They provided it

    def ping(self):
        os.system("ssh %s@%s 'supervisorctl status stream_analysis%d'" % (self.user, self.ip, self.worker_number))

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
            print "Pinging worker%d..." % i
            c.ping()


def start_all_consumers():
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


def gather_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.gather_report()


def clear_all_reports():
    for i in range(0, len(config.consumer_ips)):
        for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
            c = Consumer('root', config.consumer_ips[i], i, worker)
            c.clear_report()


def show_report():
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

                        timestamp_dict[dt] = float(result.strip())
                    except Exception as e:
                        print e
                        pass

    timestamp_list = [key for key in timestamp_dict]
    timestamp_list.sort()

    result_list = [timestamp_dict[timestamp] for timestamp in timestamp_list]

    fig, ax = plt.subplots()
    ax.plot_date(timestamp_list, result_list, linestyle="-")

    plt.show()
