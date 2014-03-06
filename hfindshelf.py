import hou
import mydebug

# Custom Print Handler
class MyHouFindResultsPrint(mydebug.houfind.HouFindResultsPrint):
    def __init__(self):
        super(MyHouFindResultsPrint, self).__init__()

    def category(self, category):
        print "{0}".format(category.upper())
    
    def data(self, data):
        print "  {0}".format(data)
    
    def item(self, item):
        print "    {0}".format(item)


# Files to find
files = (
            'scripts/123.cmd',
            'scripts/456.cmd',
            'scripts/123.py',
            'scripts/456.py',
            'OPlibraries',
            'scripts/python/pythonrc.py',
        )

# Directories to Find
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
                'help/shelf',
                'help',
              )

def execute():
    # Files Finder Object
    findFiles = mydebug.houfind.HouFind(files, 'Files', hou.findFiles, MyHouFindResultsPrint)
    
    # Directories Finder Object
    findDirectories = mydebug.houfind.HouFind(directories, 'Directories', hou.findDirectories, MyHouFindResultsPrint)
    
    # Do it
    for finder in (findFiles, findDirectories):
        finder()

