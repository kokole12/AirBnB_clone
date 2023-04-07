#!/usr/bin/python3
""" fabric scrit to deploy the .tgz file created"""
from fabric.api import *
import os.path
from os.path import exists
env.hosts=["ip add", "ip add"]

def do_deploy(archive_path):
	if exists(archibe_path) is None:
		return False
	try:
		file_name = archive_path.split("/")[-1]
		name = file_name.split(".")[0]
		path = /data/web_static/releases/
		put(archive_path, '/tmp/')
		run("mkdir -p {}{}/".format(path, name)
		run("tar -xvf /tmp/ {} -C {}{}/".format(file_name, path, name))
		run("rm -rf /tmp/{}".format(filename))
		run("mv {}{}/web_static/* {}{}".format(path, name, path,name))
		run("rm -rf {}{}/web_static".fornat(path, name))
		run("rm -rf /data/web_stattic/current")
		run("ln -s {}{}/ /data/web_static/current".format(path, name)
		return True
	except Exception as e:
		return False	
