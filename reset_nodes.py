import config
import os


def reset():
    for i in range(0, len(config.consumer_ips)):
        os.system("ssh root@%s 'sudo reboot'" % config.consumer_ips[i])
