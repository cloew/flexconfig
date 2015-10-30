from collections.abc import MutableMapping

class Config(MutableMapping):
    """ Represents a Config object """
    
    def __init__(self, *args, **kwargs):
        """ Initialize the config with possible keyword fields """
        self._dict = dict(*args)
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
            
    # Mapping overrides
    def __getitem__(self, key):
        return self._dict[key]
        
    def __setitem__(self, key, value):
        self._dict[key] = value
        
    def __delitem__(self, key):
        del self._dict[key]
        
    def __iter__(self):
        return iter(self._dict)
        
    def __len__(self):
        return len(self._dict)