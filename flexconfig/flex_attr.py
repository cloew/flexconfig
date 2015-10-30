from .get_data import getdata
from .kao_descriptor import KaoDescriptor

class FlexAttr(KaoDescriptor):
    """ Descriptor for an Attr that may exist in an underlying data store or not """
    
    def __init__(self, attr, data=None):
        """ Initialize with the attribute and the data container attr """
        self.attr = attr
        self.data = data
            
    def __getvalue__(self, obj):
        """ Return the attr value """
        data = getdata(obj, self.data)
        return data[self.attr] if self.attr in data else None
    
    def __set__(self, obj, value):
        """ Set the proper value for the attribute """
        data = getdata(obj, self.data)
        data[self.attr] = value
        
    def __delete__(self, obj):
        """ Delete the value for the attribute """
        data = getdata(obj, self.data)
        del data[self.attr]