print dir()

print
import inspect
print inspect.getfile(inspect.currentframe())
del inspect

print 'Creating new session'

sessionname = hou.hipFile.name()
if 'untitled.hip' in sessionname:
    print "Remember to save your file"

print "Setting my preferred desktop"

if hou.isUIAvailable():
    desktops = dict((desktop.name(), desktop) for desktop in hou.ui.desktops())

    if 'MyTechnical' in desktops:
        desktops['MyTechnical'].setAsCurrent()
        
    del desktops

del sessionname

