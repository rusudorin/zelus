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

    os.system('scp ' + arguments + ' -r ' + get_current_folder() + '/' + deployment + ' ' + user + '@' + host + ':' + root_folder + user)


# prepares and copies the templating file
def prepare_template(deployment, user, host, substitution_dict, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    filein = open(get_current_folder() + '/templating/apply_template_template.py')
    src = Template(filein.read())

    d = {"templ_module_name": deployment, "templ_substitution_dict": substitution_dict}
    result = src.safe_substitute(d)

    if deployment == 'stormtrooper':
        fileout = open(get_current_folder() + '/templating/apply_template' + '_' + substitution_dict['templ_worker_name'] + '.py', 'w')
    else:
        fileout = open(get_current_folder() + '/templating/apply_template.py', 'w')
    fileout.write(result)
    fileout.close()

    if deployment == 'stormtrooper':
        os.system('scp ' + arguments + get_current_folder() + '/templating/apply_template' + '_' + substitution_dict['templ_worker_name'] + '.py ' + user + '@' + host + ':' + root_folder + user + '/' + deployment + '/apply_template.py')
    else:
        os.system('scp ' + arguments + get_current_folder() + '/templating/apply_template.py ' + user + '@' + host + ':' + root_folder + user + '/' + deployment + '/apply_template.py')
# TODO - delete file


# initiates the installation of a deployment on a new machine
def install_deployment(deployment, user, host, substitution_dict, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    change_dir = 'cd ' + root_folder + user + '/' + deployment
    apply_template = 'python apply_template.py'
    install_location = 'sh ' + root_folder + user + '/' + deployment + '/install.sh'

    action = change_dir + ';' + apply_template + ';' + install_location
    os.system("ssh " + arguments + " " + user + "@" + host + " " + "'" + action + "'")


# start rpcs on each consumer
def start_rpc(deployment, user, host, deployment_folder, arguments=''):
    if deployment == 'stormtrooper':
        action = 'nohup python ' + deployment_folder + '/rpc_consumer.py < /dev/null > std.out 2> std.err &'
        command = "ssh " + arguments + " " + user + "@" + host + " " + "'" + action + "'"
        os.system(command)


# sets up deployment
def deploy(deployment, user, host, substitution_dict, arguments=''):
    copy_deployment(deployment, user, host)
    prepare_template(deployment, user, host, substitution_dict)
    install_deployment(deployment, user, host, substitution_dict)
    start_rpc(deployment, user, host, substitution_dict)
