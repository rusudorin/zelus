from deploy import *
from consumer_control import start_all_consumers, stop_all_consumers, gather_all_reports, clear_all_reports, \
    ping_all, show_report
from populate_emperor import populate_read, populate_write, populate_update
from populate_rebels import do_populate
from zelus.stormtrooper import Stormtrooper
import cmd
import config
import const


class Zelush(cmd.Cmd):

    prompt = 'zelush> '
    
    # nosql deployment
    def do_deploy_nosql(self, nosql):
        """Deploys a nosql datastore
        deploy_nosql [nosql]"""
        try:
            if nosql not in const.nosql_list:
                print "No such nosql available"
                return

            for nosql_obj in config.nosql_ips:
                nosql_ip = nosql_obj[0]
                nosql_user = nosql_obj[1]

                if nosql == 'cassandra':
                    deploy_cassandra(nosql_user, nosql_ip)
                if nosql == 'mongodb':
                    deploy_mongodb(nosql_user, nosql_ip)
                if nosql == 'riak':
                    deploy_riak(nosql_user, nosql_ip)
                if nosql == 'redis':
                    deploy_redis(nosql_user, nosql_ip)
                if nosql == 'bigcouch':
                    deploy_bigcouch(nosql_user, nosql_ip)
                if nosql == 'hbase':
                    deploy_hbase(nosql_user, nosql_ip)
        except Exception as e:
            print e

    def complete_deploy_nosql(self, text, line, begidx, endidx):
        if not text:
            completions = const.nosql_list
        else:
            completions = [f for f in const.nosql_list if f.startswith(text)]
        return completions

    # emperor deployment
    def do_deploy_emperor(self, line=None):
        """Deploys the emperor nodes"""
        process_list = []

        for emperor_obj in config.emperor_ips:
            # emperor_obj is a list [ip, user]
            p = deploy_emperor((emperor_obj[1], emperor_obj[0]))

            process_list.append(p)

        for p in process_list:
            p.join()

    # stormtrooper deployment
    def do_deploy_stormtrooper(self, nosql=None):
        """Deploy stormtroopers to all nodes mentioned in the config file
        deploy_stormtrooper [noslq]"""
        try:
            if nosql not in const.nosql_list:
                print "No such nosql available"
                return

            process_list = []

            for i in range(0, len(config.stormtrooper_ips)):
                storm_ip = config.stormtrooper_ips[i][0]
                storm_user = config.stormtrooper_ips[i][1]

                p = stormtrooper((storm_user, storm_ip, nosql, i, config.concurrency,
                                  config.stormtrooper_numbers[storm_ip]))
                process_list.append(p)

            for p in process_list:
                p.join()

        except Exception as e:
            print e

    def complete_deploy_stormtrooper(self, text, line, begidx, endidx):
        if not text:
            completions = const.nosql_list
        else:
            completions = [f for f in const.nosql_list if f.startswith(text)]
        return completions

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
            completions = const.nosql_list
        else:
            completions = [f for f in const.nosql_list if f.startswith(text)]
        return completions

    # populate emperor with read tasks for all stormtroopers
    def do_populate_read(self, line):
        """Populate emperor with read tasks for all stormtroopers
        populate_read [nosql] [amount]"""
        try:
            nosql, amount = line.split(" ")
            process_list = []

            for i in range(0, len(config.stormtrooper_ips)):
                storm_ip = config.stormtrooper_ips[i][0]
                storm_user = config.stormtrooper_ips[i][1]

                for j in range(0, config.stormtrooper_numbers[storm_ip]):
                    c = Stormtrooper(storm_user, storm_ip, i, j)
                    p = populate_read((nosql, c, int(amount)))
                    process_list.append(p)
            
            for p in process_list:
                p.join()

        except Exception as e:
            print e

    def complete_populate_read(self, text, line, begidx, endidx):
        if not text:
            completions = const.nosql_list
        else:
            completions = [f for f in const.nosql_list if f.startswith(text)]
        return completions

    # populate emperor with write tasks for all stormtroopers
    def do_populate_write(self, line):
        """Populate emperor with write tasks for all stormtroopers
        populate_write [amount] [granularity]"""
        try:
            amount, granularity = line.split(" ")
            process_list = []

            for i in range(0, len(config.stormtrooper_ips)):
                storm_ip = config.stormtrooper_ips[i][0]
                storm_user = config.stormtrooper_ips[i][1]

                for j in range(0, config.stormtrooper_numbers[storm_ip]):
                    c = Stormtrooper(storm_user, storm_ip, i, j)
                    p = populate_write((c, int(amount), int(granularity)))
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

            for i in range(0, len(config.stormtrooper_ips)):
                storm_ip = config.stormtrooper_ips[i][0]
                storm_user = config.stormtrooper_ips[i][1]

                for j in range(0, config.stormtrooper_numbers[storm_ip]):
                    c = Stormtrooper(storm_user, storm_ip, i, j)
                    p = populate_update((nosql, c, int(amount), int(granularity)))
                    process_list.append(p)

            for p in process_list:
                p.join()
        except Exception as e:
            print e

    def complete_populate_update(self, text, line, begidx, endidx):
        if not text:
            completions = const.nosql_list
        else:
            completions = [f for f in const.nosql_list if f.startswith(text)]
        return completions

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
