import os

ROOT_DIR = os.getcwd()
py2_dir = ROOT_DIR + '/python2-version'
py3_dir = ROOT_DIR + '/python3-version'

def translate(typ, directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			filename = os.path.join(root, file)
			if os.path.splitext(filename)[1] == 'bak':
				os.remove(filename)

				#2to3
				cmd = typ + ' -w ' + filename
				os.system(cmd)


#translate('2to3', py2_dir)
translate('3to2', py3_dir)