from deploy_infrastructure.deploy_helper import copy_deployment, prepare_template, install_deployment

import config
import const

# launch an emperor node
def deploy_emperor(user, host):
    d = {
            "templ_rabbit_ip": config.rabbit_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost
        }
    copy_deployment('emperor', user, host)
    prepare_template('emperor', user, host, d)
    install_deployment('emperor', user, host)

# launch a stormtrooper
def deploy_stormtrooper(user, host, nosql, worker_name, concurrency, queue):

    if nosql not in const.nosql_list:
        return "Nope"

    d = {
            "templ_rabbit_ip": config.rabbit_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost,
            "templ_nosql_ip": config.nosql_ip,
            "templ_deploy_home": "/home/" + user,
            "templ_handler_name": nosql + "_handler",
            "templ_handler_class": const.nosql_classes[nosql],
            "templ_extra_package": "",
            "templ_worker_name": worker_name,
            "templ_concurrency": concurrency,
            "templ_consume_queue": queue,
            "templ_current_ip": host,
            "templ_user_ip": config.user_ip
        }

    copy_deployment('stormtrooper', user, host)
    prepare_template('stormtrooper', user, host, d)
    install_deployment('stormtrooper', user, host)
