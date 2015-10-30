from .kao_descriptor import KaoDescriptor
import os

class ConfigPath(KaoDescriptor):
    """ Descriptor to access a Config Path """
    
    def __init__(self, pathAttr):
        """ Initialize with the pathAttr """
        self.pathAttr = pathAttr
            
    def __getvalue__(self, obj):
        """ Return the attr value """
        path = self.storedPath(obj)
        if path is None:
            return path
            
        configDir = self.configDir(obj)
        return os.path.normpath(os.path.join(configDir, path))
    
    def __set__(self, obj, value):
        """ Set the proper value for the attribute """
        configDir = self.configDir(obj)
        path = os.path.relpath(value, start=configDir)
        setattr(obj, self.pathAttr, path)
        
    def storedPath(self, obj):
        """ Return the Stored Path """
        return getattr(obj, self.pathAttr) if hasattr(obj, self.pathAttr) else None
        
    def configDir(self, obj):
        """ Return the Config Directory """
        return os.path.dirname(obj.filename)