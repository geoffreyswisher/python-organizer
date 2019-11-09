# Moves files with given extensions in the current 
# directory to extension-specific folders

import os
import shutil

# the extensions to be moved
extensions = ['.py', '.sh']

# the path to the directory to be organized
pathtodir = '.'

for file in os.listdir(pathtodir):

    for extension in extensions:

        if file.find(extension) == len(file)-len(extension) and file != 'organizer.py':

            dirname = extension[1::] + 'files' 

            #to catch errors with making a directory that already exists
            try:
                os.mkdir(dirname)
            except OSError:
                pass
            else: 
                print('created new directory:\t%s', dirname)
            
            path = './%s/' % (dirname)
            shutil.move(file, path)
            print('Moving %s to %s' % (file, path))
