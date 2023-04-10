import importlib
from torch import nn

class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__() # super() is a built-in function that returns a proxy object (temporary object of the superclass) that allows you to refer parent class by 'super' instead of 'self'. The proxy object delegates method calls to the parent class or to a sibling class.


def initModel(model_name : str):

    # TODO: logger

    model_path = "FLite.models.{}".format(model_name)
    model_lib = importlib.import_module(model_path)
    model = getattr(model_lib, "Model")
    return model