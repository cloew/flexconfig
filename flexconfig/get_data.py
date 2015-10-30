
def getdata(obj, dataAttr):
    return obj if dataAttr is None else getattr(obj, dataAttr)