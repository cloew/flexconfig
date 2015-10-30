
class WrapperHelper:
    """ Helper class to facilitate wrapping objects in the Wrapper Class """
    
    def __init__(self, wrapperCls):
        """ Initailize with the wrapper class """
        self.wrapperCls = wrapperCls
        
    def instantiate(self, *args, **kwargs):
        """ Instantiate the wrapper class with the given arguments """
        return self.wrapperCls(*args, **kwargs)
        
    def wrapIfNeeded(self, obj, *args, **kwargs):
        """ Wrap the given object if it is not already wrapped """
        if not isinstance(obj, self.wrapperCls):
            obj = self.instantiate(obj, *args, **kwargs)
        return obj