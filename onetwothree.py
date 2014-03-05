import hou

print dir()

print
import inspect
print inspect.getfile(inspect.currentframe())
del inspect

import mydebug

files = (
            'scripts/123.cmd',
            'scripts/456.cmd',
            'scripts/123.py',
            'scripts/456.py',
            'OPlibraries',
            'scripts/python/pythonrc.py',
        )

#inputFiles = mydebug.houfind.HouFindInput(files, 'Files')
        
directories = (
                'config',
                'scripts',
                'presets',
                'dso',
                'custom',
                'desktop',
                'func',
                'otls',
                'shop',
                'toolbar',
                'vex',
                'python',
                'scripts/python',
              )

#inputDirectories = mydebug.houfind.HouFindInput(directories, 'Directories')
              
findFiles = mydebug.houfind.HouFind(files, 'Files', hou.findFiles)
findDirectories = mydebug.houfind.HouFind(directories, 'Directories', hou.findDirectories)

for finder in (findFiles, findDirectories):
    finder()

del files
del findFiles

del directories
del findDirectories

del finder

if 'houdiniInterpreter' in globals():
    hi = houdiniInterpreter


