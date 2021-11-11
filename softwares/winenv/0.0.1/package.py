name = "winenv"

version = "0.0.1"

authors = [
	"Joey"
]

description = \
	"""
	A dummy package to initialize dev env.
	"""

tools = [
]

requires = [
	"python"
]

variants = [
	["platform-windows", "arch-AMD64"],
]

uuid = "softwares.winenv"

build_command = "python {root}/build.py {install}"


def commands():
	# Hard coded for now
	import os
	os.system('call C:/"Program Files (x86)/Microsoft Visual Studio"/2019/Community/VC/Auxiliary/Build/vcvarsall.bat amd64')
	os.environ['PATH'] = ';'.join([os.environ['PATH'], 'C:/Program Files (x86)/Windows Kits/10/bin/10.0.19041.0/x64'])