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

    os.system("scp {0} -r {1}/{2} {3}@{4}:{5}{6}".
              format(arguments, get_current_folder(), deployment, user, host, root_folder, user))


# copies extra files to puppet folder on the new machine
def copy_extras(handler, user, host, arguments=''):
    os.system("scp {0} {1}/../nosql_handlers/{2}.py {3}@{4}:{5}/{3}/stormtrooper/modules/stormtrooper/files/".
              format(arguments, get_current_folder(), handler, user, host, root_folder))
    os.system("scp {0} {1}/../nosql_handlers/nosql_handler.py {2}@{3}:{4}/{2}/stormtrooper/modules/stormtrooper/files/".
              format(arguments, get_current_folder(), user, host, root_folder))
    os.system("scp {0} {1}/../data_gen.py {2}@{3}:{4}/{2}/stormtrooper/modules/stormtrooper/files/".
              format(arguments, get_current_folder(), user, host, root_folder))
    os.system("scp {0} {1}/../const.py {2}@{3}:{4}/{2}/stormtrooper/modules/stormtrooper/files/".
              format(arguments, get_current_folder(), user, host, root_folder))


# prepares and copies the templating file
def prepare_template(deployment, user, host, substitution_dict, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    filein = open("{0}/templating/apply_template.temp".format(get_current_folder()))
    src = Template(filein.read())

    d = {
        "templ_module_name": deployment,
        "templ_substitution_dict": substitution_dict
    }
    result = src.safe_substitute(d)

    fileout = open("{0}/templating/apply_template_{1}.py".format(get_current_folder(), host), 'w')
    fileout.write(result)
    fileout.close()

    os.system("scp {0} {1}/templating/apply_template_{2}.py {3}@{2}:{4}{3}/{5}/apply_template.py".
              format(arguments, get_current_folder(), host, user, root_folder, deployment))
    os.remove("{0}/templating/apply_template_{1}.py".format(get_current_folder(), host))


# initiates the installation of a deployment on a new machine
def install_deployment(deployment, user, host, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    change_dir = "cd {0}{1}/{2}".format(root_folder, user, deployment)
    apply_template = 'python apply_template.py'
    install_location = "sh {0}{1}/{2}/install.sh".format(root_folder, user, deployment)

    action = change_dir + ';' + apply_template + ';' + install_location
    os.system("ssh {0} {1}@{2} '{3}'".format(arguments, user, host, action))


# sets up deployment
def deploy(deployment, user, host, substitution_dict, arguments=''):
    copy_deployment(deployment, user, host)
    if deployment == 'stormtrooper':
        copy_extras(substitution_dict['templ_handler_name'], user, host)
    prepare_template(deployment, user, host, substitution_dict)
    install_deployment(deployment, user, host)
