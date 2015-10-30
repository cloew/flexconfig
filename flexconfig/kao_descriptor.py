
class KaoDescriptor:
    """ Base Descriptor class """
    
    def __get__(self, obj, type=None):
        """ Get the proper value for the attribute """
        if type is None:
            return self
        else:
            return self.__getvalue__(obj)