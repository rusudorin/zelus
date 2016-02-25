import os
from string import Template

deployment_options = ['emperor', 'stormtrooper']
root_folder = '/'


# returns the current folder of the file
def get_current_folder():
    return os.path.dirname(os.path.realpath(__file__))


# copies a deployment to a new machine
def copy_deployment(deployment, user, host, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    os.system("scp %s -r %s/%s %s@%s:%s%s" %
              (arguments, get_current_folder(), deployment, user, host, root_folder, user))


# prepares and copies the templating file
def prepare_template(deployment, user, host, substitution_dict, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    filein = open("%s/templating/apply_template.temp" % get_current_folder())
    src = Template(filein.read())

    d = {
        "templ_module_name": deployment,
        "templ_substitution_dict": substitution_dict
    }
    result = src.safe_substitute(d)

    if deployment == 'stormtrooper':
        fileout = open("%s/templating/apply_template_%s.py" %
                       (get_current_folder(), substitution_dict['templ_worker_name']), 'w')
    else:
        fileout = open("%s/templating/apply_template.py" % get_current_folder(), 'w')
    fileout.write(result)
    fileout.close()

    if deployment == 'stormtrooper':
        os.system("scp %s %s/templating/apply_template_%s.py %s@%s:%s%s/%s/apply_template.py" %
                  (arguments, get_current_folder(), substitution_dict['templ_worker_name'],
                   user, host, root_folder, user, deployment))
    else:
        os.system("scp %s %s/templating/apply_template.py %s@%s:%s%s/%s/apply_template.py" %
                  (arguments, get_current_folder(), user, host, root_folder, user, deployment))
# TODO - delete file


# initiates the installation of a deployment on a new machine
def install_deployment(deployment, user, host, substitution_dict, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    change_dir = "cd %s%s/%s" % (root_folder, user, deployment)
    apply_template = 'python apply_template.py'
    install_location = "sh %s%s/%s/install.sh" % (root_folder, user, deployment)

    action = change_dir + ';' + apply_template + ';' + install_location
    os.system("ssh %s %s@%s '%s'" % (arguments, user, host, action))


# start rpcs on each consumer
def start_rpc(deployment, user, host, deployment_folder, arguments=''):
    if deployment == 'stormtrooper':
        action = 'nohup python ' + deployment_folder + '/rpc_consumer.py < /dev/null > std.out 2> std.err &'
        command = "ssh %s %s@%s '%s'" % (arguments, user, host, action)
        os.system(command)


# sets up deployment
def deploy(deployment, user, host, substitution_dict, arguments=''):
    copy_deployment(deployment, user, host)
    prepare_template(deployment, user, host, substitution_dict)
    install_deployment(deployment, user, host, substitution_dict)
    start_rpc(deployment, user, host, substitution_dict)
