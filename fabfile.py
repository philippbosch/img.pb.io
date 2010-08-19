import os.path
from fabric.api import *

env.project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
env.user_name = 'pb'

# ------ environments ----------    
def staging():
    """Deploy on staging host"""
    env.hosts = ['%(user_name)s@srv.aotp.de' % env]
    env.path = '/home/%(user_name)s/projects/%(project_name)s' % env
    
def production():
    """Deploy master branch on live server"""
    env.hosts = ['%(user_name)s@srv.aotp.de' % env]
    env.path = '/home/%(user_name)s/projects/%(project_name)s' % env

# --------- commands -----------
# def rebase():
#     local('git checkout master')
#     local('git rebase develop')
#     local('git checkout develop')

def deploy_only():
    local("git push origin master" % env)
    with cd(env.path):
        run("git pull origin master" % env)

def deploy():
    deploy_only()
    migrate()
    run("touch %(path)s/deploy/project.wsgi" % env)

def migrate():
    with cd(env.path):
        run("../../.virtualenvs/%(project_name)s/bin/python ./manage.py syncdb" % env)
        run("../../.virtualenvs/%(project_name)s/bin/python ./manage.py migrate" % env)
        run("touch %(path)s/deploy/project.wsgi" % env)
