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


# copies extra files to puppet folder on the new machine
def copy_extras(handler, user, host, arguments=''):
    os.system("scp %s %s/../nosql_handlers/%s.py %s@%s:%s/%s/stormtrooper/modules/stormtrooper/files/" %
              (arguments, get_current_folder(), handler, user, host, root_folder, user))
    os.system("scp %s %s/../nosql_handlers/nosql_handler.py %s@%s:%s/%s/stormtrooper/modules/stormtrooper/files/" %
              (arguments, get_current_folder(), user, host, root_folder, user))


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

    fileout = open("%s/templating/apply_template_%s.py" % (get_current_folder(), host), 'w')
    fileout.write(result)
    fileout.close()

    os.system("scp %s %s/templating/apply_template_%s.py %s@%s:%s%s/%s/apply_template.py" %
              (arguments, get_current_folder(), host, user, host, root_folder, user, deployment))
    os.remove("%s/templating/apply_template_%s.py" % (get_current_folder(), host))


# initiates the installation of a deployment on a new machine
def install_deployment(deployment, user, host, arguments=''):
    if deployment not in deployment_options:
        return 'Not a deployment'

    change_dir = "cd %s%s/%s" % (root_folder, user, deployment)
    apply_template = 'python apply_template.py'
    install_location = "sh %s%s/%s/install.sh" % (root_folder, user, deployment)

    action = change_dir + ';' + apply_template + ';' + install_location
    os.system("ssh %s %s@%s '%s'" % (arguments, user, host, action))


# sets up deployment
def deploy(deployment, user, host, substitution_dict, arguments=''):
    copy_deployment(deployment, user, host)
    if deployment == 'stormtrooper':
        copy_extras(substitution_dict['templ_handler_name'], user, host)
    prepare_template(deployment, user, host, substitution_dict)
    install_deployment(deployment, user, host)
