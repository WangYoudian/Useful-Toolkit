import os

def TraverseFolder(folderpath):
    for root, dirs, files in os.walk(folderpath, topdown=True):
        for file in files:
            filename = os.path.join(root, file)
            if os.path.splitext(filename)[1] == '.py':
                print(filename)
                cmd = "2to3 -n -w " + filename
                os.system(cmd)
        if dirs:
	        for directory in dirs:
	            TraverseFolder(directory)

if __name__ == '__main__':
	# Put you target folder here
    localfolder = 'C:/Users/win10/Downloads/pwcracker-master/pwcracker-master'
    print(localfolder)
    TraverseFolder(localfolder)
    # time costs 20s for paddlepaddle tutorial