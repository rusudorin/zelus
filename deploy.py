from deploy_infrastructure import deploy_helper
import os

deploy_helper.prepare_template('emperor', 'root', '10.141.0.154', {})
