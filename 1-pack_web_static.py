#!/usr/bin/python3
""" Pythom script to generate a .tgz file"""
from fabric.api import *
from datetime import datetime

@task
def do_pack():
	time = datetime.now()
	file_name = "web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S")

	local("mkdir -p versions")
	create_file = locol("tar -cvfz versins/{} webstatic/'.format(file_name))
	if create_file is not None:
		return file_name
	else:
		return None
	
