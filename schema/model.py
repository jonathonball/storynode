from .loader.yaml import YamlLoader

class Model:

    Name = None

    def __init__(self, name, loader='yaml'):
        self.Name = name
        self.setLoader(loader)

    def setLoader(self, loader):
        if (loader == 'yaml'):
            self.loader = YamlLoader()
        elif (loader == 'json'):
            raise NotImplementedError('json not yet implemented')
        else:
            raise TypeError('Unknown loader type: ' + loader)
