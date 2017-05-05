# coding: utf-8
from fabric.api import run, env, cd


def deploy():
    """部署"""
    env.host_string = "user@server"
    with cd('/path/to/project'):
        run('git pull')
        run('npm install')
        run('npm run build')
