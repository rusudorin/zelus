import os


class Rebel:
    def __init__(self, ip):
        self.ip = ip

    def ping(self):
        print "\nPinging rebel {0}...".format(self.ip)

        os.system("ssh {0}@{1} 'supervisorctl status cpu_usage'".format('root', self.ip))
        os.system("ssh {0}@{1} 'supervisorctl status cpu_load'".format('root', self.ip))
        # TODO move users to config

    def start_monitoring(self):
        print "Starting nosql {0}".format(self.ip)

        os.system("ssh {0}@{1} 'supervisorctl start cpu_usage'".format('root', self.ip))
        os.system("ssh {0}@{1} 'supervisorctl start cpu_load'".format('root', self.ip))
        # TODO move users to config

    def stop_monitoring(self):
        print "Stopping nosql {0}".format(self.ip)

        os.system("ssh {0}@{1} 'supervisorctl stop cpu_usage'".format('root', self.ip))
        os.system("ssh {0}@{1} 'supervisorctl stop cpu_load'".format('root', self.ip))
        # TODO move users to config

    def gather_report(self):
        print "Gathering report from {0}".format(self.ip)

        os.system("scp {0}@{1}:/var/log/supervisor/cpu_usage.out cpu_usage_nosql{1}.out".format('root', self.ip))
        os.system("scp {0}@{1}:/var/log/supervisor/cpu_load.out cpu_load_nosql{1}.out".format('root', self.ip))
        # TODO move users to config

    def clear_report(self):
        print "Clearing report from {0}".format(self.ip)

        os.system("ssh {0}@{1} 'rm /var/log/supervisor/cpu_usage.out'".format('root', self.ip))
        os.system("ssh {0}@{1} 'rm /var/log/supervisor/cpu_load.out'".format('root', self.ip))
        # TODO move users to config










