#!/usr/bin/python3
from fabric.api import *
from os.path import exists
env.hosts=["ip", "ip"]
import time

def do_pack():
	local("mkdir -p versions")
	create = local("tar -cvzf versions/web_static_{}.tgz web_static".format(time.strftime("%Y%m%d%H%M%S")))
	if create is not None:
		return versions/web_static_{}.tgz web_static".format(time.strftime("%Y%m%d%H%M%S"))
	else:
		return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
	archive_path = do_pack()
	if archive_path is None:
		return False
	else:
		do_deploy(archive_path)

