import platform
OS = platform.system().lower()

print("Running on '%s' platform." % OS)

# default values for options
DEBUG = False
HOST = 'localhost'
PORT = 7525


if OS == 'windows':
	# debug configuration (dev)
	DEBUG = True

elif OS == 'linux':
	# deploy configuration (test & production)
	DEBUG = False
	HOST = "109.206.169.214"

else:
	pass

