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
def deploy_stormtrooper(user, host, nosql):

    if nosql not in const.nosql_list:
        return "Nope"

    d = {
            "templ_rabbit_ip": config.rabbit_ip,
            "templ_rabbit_user": config.rabbit_user,
            "templ_rabbit_pass": config.rabbit_pass,
            "templ_rabbit_vhost": config.rabbit_vhost,
            "templ_nosql_ip": config.nosql_ip,
            "templ_deploy_home": "/home/" + user,
            "templ_handler_name": nosql + "_handler.py",
            "templ_extra_package": ""
        }

    copy_deployment('stormtrooper', user, host)
    prepare_template('stormtrooper', user, host, d)
    install_deployment('stormtrooper', user, host)
