from .wrapper_helper import WrapperHelper
from collections.abc import MutableSequence

class WrapperList(MutableSequence):
    """ Represents a list where all the elements should be wrpped with a type """
    
    def __init__(self, *args, wrapperCls):
        """ Initialize with the wrapper class """
        self.wrapper = WrapperHelper(wrapperCls)
        self._lst = list(*args)
        
    def __iter__(self):
        """ Return the values in the List """
        for i in range(len(self)):
            yield self[i]
        
    def __getitem__(self, index):
        """ Return the proper item """
        value = self._lst[index]
        self[index] = value # Force the wrapping of the underlying value
        return self._lst[index]
        
    def __setitem__(self, index, value):
        """ Set the proper index """
        value = self.wrapper.wrapIfNeeded(value)
        self._lst[index] = value
        
    def __delitem__(self, index):
        """ Delete the item at the given index """
        del self._lst[index]
        
    def __len__(self):
        """ Return the length of the list """
        return len(self._lst)
        
    def insert(self, index, value):
        """ Insert the value at the given position """
        value = self.wrapper.wrapIfNeeded(value)
        self._lst.insert(index, value)