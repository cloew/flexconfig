from .get_data import getdata
from .kao_descriptor import KaoDescriptor
from .wrapper_helper import WrapperHelper

class WrappedAttr(KaoDescriptor):
    """ Represents an attribute that should be wrapped in a class before being returned """
    
    def __init__(self, attr, wrapperCls, data=None, args=[], kwargs={}):
        """ Initialize with the attr to wrap, the cls and the data container attr """
        self.attr = attr
        self.wrapper = WrapperHelper(wrapperCls)
        self.data = data
        self.args = args
        self.kwargs = kwargs
            
    def __getvalue__(self, obj):
        """ Return the attr value """
        data = getdata(obj, self.data)
        if self.attr not in data:
            data[self.attr] = self.wrapper.instantiate(*self.args, **self.kwargs)
        value = data[self.attr]
        self.__set__(obj, value)
        return data[self.attr]
    
    def __set__(self, obj, value):
        """ Set the proper value for the attribute """
        data = getdata(obj, self.data)
        value = self.wrapper.wrapIfNeeded(value, *self.args, **self.kwargs)
        data[self.attr] = value
        
    def __delete__(self, obj):
        """ Delete the value for the attribute """
        data = getdata(obj, self.data)
        del data[self.attr]