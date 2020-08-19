from .loader.yaml import YamlLoader
from .loader.json import JsonLoader

class Model:

    Name = None

    def __init__(self, name, loader='yaml'):
        self.Name = name
        self.setLoader(loader)

    def setLoader(self, loader):
        if (loader == 'yaml'):
            self.loader = YamlLoader()
        elif (loader == 'json'):
            self.loader = JsonLoader()
        else:
            raise TypeError('Unknown loader type: ' + loader)
