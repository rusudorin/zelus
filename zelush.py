from deploy import *
from populate_rebels import do_populate
from populate_emperor import populate_read, populate_write, populate_update
from consumer_control import start_all_consumers, stop_all_consumers, gather_all_reports, clear_all_reports, \
    ping_all, show_report
import cmd
import config
import const


class Zelush(cmd.Cmd):

    prompt = 'zelush> '
    
    # nosql deployment
    def do_deploy_nosql(self, line):
        """Deploys a nosql datastore
        deploy_nosql [nosql] [user] [host]"""
        try:
            nosql, user, host = line.split(' ')

            if not nosql or not user or not host:
                print "Mising arguments"
                return

            if nosql not in const.nosql_list:
                print "No such nosql available"
                return 

            else:
                if nosql == 'cassandra':
                    deploy_cassandra(user, host)
                if nosql == 'mongodb':
                    deploy_mongodb(user, host)
                if nosql == 'riak':
                    deploy_riak(user, host)
                if nosql == 'redis':
                    deploy_redis(user, host)
                if nosql == 'bigcouch':
                    deploy_bigcouch(user, host)
                if nosql == 'hbase':
                    deploy_hbase(user, host)
        except Exception as e:
            print e

    def complete_deploy_nosql(self, text, line, begidx, endidx):
        if not text:
            completitions = const.nosql_list
        else:
            completitions = [f for f in const.nosql_list if f.startswith(text)]
        return completitions

    # emperor deployment
    def do_deploy_emperor(self, line):
        """Deploys an emperor node
        deploy_emperor [user] [host] """
        try:
            user, host = line.split(" ")
            deploy_emperor(user, host)
        except Exception as e:
            print e

    # stormtrooper deployment
    def do_deploy_stormtrooper(self, nosql=None):
        """Deploy stormtroopers to all nodes mentioned in the config file
        deploy_stormtrooper [noslq]"""
        try:
            if nosql not in const.nosql_list:
                print "No such nosql available"
                return

            process_list = []

            for i in range(0, len(config.consumer_ips)):
                p = stormtrooper(('root', config.consumer_ips[i], nosql, i,
                                 config.concurrency, config.worker_numbers[config.consumer_ips[i]]))
                process_list.append(p)

            for p in process_list:
                p.join()

        except Exception as e:
            print e

    def complete_deploy_stormtrooper(self, text, line, begidx, endidx):
        if not text:
            completitions = const.nosql_list
        else:
            completitions = [f for f in const.nosql_list if f.startswith(text)]
        return completitions

    # populate rebels (nosqls)
    def do_populate_rebels(self, line):
        """Populate the nosql datastores
        populate_rebels [nosql] [granularity] [total_size]"""
        try:
            nosql, granularity, total_size = line.split(" ")
            do_populate(nosql, int(granularity), int(total_size))
        except Exception as e:
            print e

    def complete_populate_rebels(self, text, line, begidx, endidx):
        if not text:
            completitions = const.nosql_list
        else:
            completitions = [f for f in const.nosql_list if f.startswith(text)]
        return completitions

    # populate emperor with read tasks for all stormtroopers
    def do_populate_read(self, line):
        """Populate emperor with read tasks for all stormtroopers
        populate_read [nosql] [amount]"""
        try:
            nosql, amount = line.split(" ")
            process_list = []

            for i in range(0, len(config.consumer_ips)):
                for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
                    p = populate_read((nosql, "worker%d_%d" % (i, worker), int(amount)))
                    process_list.append(p)
            
            for p in process_list:
                p.join()

        except Exception as e:
            print e

    def complete_populate_read(self, text, line, begidx, endidx):
        if not text:
            completitions = const.nosql_list
        else:
            completitions = [f for f in const.nosql_list if f.startswith(text)]
        return completitions

    # populate emperor with write tasks for all stormtroopers
    def do_populate_write(self, line):
        """Populate emperor with write tasks for all stormtroopers
        populate_write [amount] [granularity]"""
        try:
            amount, granularity = line.split(" ")
            process_list = []

            for i in range(0, len(config.consumer_ips)):
                for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
                    p = populate_write(("worker%d_%d" % (i, worker), int(amount), int(granularity)))
                    process_list.append(p)

            for p in process_list:
                p.join()
        except Exception as e:
            print e

    # populate emperor with update tasks for all stormtroopers
    def do_populate_update(self, line):
        """Populate emperor with update tasks for all stormtroopers
        populate_update [nosql] [amount] [granularity]"""
        try:
            nosql, amount, granularity = line.split(" ")
            process_list = []

            for i in range(0, len(config.consumer_ips)):
                for worker in range(0, config.worker_numbers[config.consumer_ips[i]]):
                    p = populate_update((nosql, "worker%d_%d" % (i, worker), int(amount), int(granularity)))
                    process_list.append(p)

            for p in process_list:
                p.join()
        except Exception as e:
            print e

    def complete_populate_update(self, text, line, begidx, endidx):
        if not text:
            completitions = const.nosql_list
        else:
            completitions = [f for f in const.nosql_list if f.startswith(text)]
        return completitions

    # ping all consumers
    def do_ping(self, line):
        """Ping all consumers"""
        ping_all()

    # start all consumers
    def do_start_consumers(self, line):
        """Starts all consumers"""
        start_all_consumers()

    # stop all consumers
    def do_stop_consumers(self, line):
        """Stop all consumers"""
        stop_all_consumers()

    # gather all reports
    def do_gather_reports(self, line):
        """Gather reports from all consumers"""
        gather_all_reports()

    # clear all reports
    def do_clear_reports(self, line):
        """Clear reports from all consumers"""
        clear_all_reports()

    # show reports
    def do_show(self, line):
        """Show reports"""
        show_report()

    def do_EOF(self, line):
        return True

    def do_exit(self, line):
        return True

if __name__ == '__main__':
    Zelush().cmdloop()