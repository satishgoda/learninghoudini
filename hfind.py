import inspect
print inspect.getfile(inspect.currentframe())
del inspect

import hou

##############################################################################

class HouFindInput(object):
    def __init__(self, data, category):
        self._data = data
        self._category = category
    
    @property
    def data(self):
        return self._data
    
    @property
    def category(self):
        return self._category

##############################################################################

class HouFindResult(object):
    def __init__(self, input):
        self._category = input.category
        self._data = dict().fromkeys(input.data)
    
    @property
    def category(self):
        return self._category
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data.__setitem__(*value)
    
    def update(self, value):
        self.data = value


##############################################################################

class HouFindResultsPrint(object):
    def category(self, category):
        print "\n{0}\n\t\t{1}\n{0}\n".format('-'*79, category)
    
    def data(self, data):
        print data

    def item(self, item):
        print "\t{0}".format(item)
    
    def __call__(self, results):
        self.category(results.category)
        for data in results.data:
            self.data(data)
            for item in results.data[data]:
                self.item(item)


##############################################################################

class HouFind(object):
    def __init__(self, findList, category, handler, HouFindResultsPrint=HouFindResultsPrint):
        self._input = HouFindInput(findList, category)
        self._handler = handler
        self._results = HouFindResult(self.input)
        self._printHandler = HouFindResultsPrint()
    
    @property
    def input(self):
        return self._input
    
    @property
    def results(self):
        return self._results
    
    @property
    def printHandler(self):
        return self._printHandler
    
    def _foundOrNot(self, item):
        try:
            founditems = self._handler(item)
        except hou.OperationFailed as e:
            self.results.update((item, (e.instanceMessage(),)))
        else:
            self.results.update((item, founditems))
    
    def _find(self):
        for item in self.input.data:
            self._foundOrNot(item)
    
    def __call__(self, *args):
        self._find(*args)
        self.printHandler(self.results)

