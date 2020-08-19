import os
import configparser
# #from schema import Model
# #from schema import Finder

# print(CONFIG['DEFAULT']['data_directory'])

class StoryNode:

    def __init__(self):
        self.setupConfig()

    def setupConfig(self):
        config = configparser.ConfigParser()
        config['DEFAULT']['script_directory'] = os.path.dirname(os.path.abspath(__file__))
        config['DEFAULT']['data_directory'] = os.path.join(config['DEFAULT']['script_directory'], 'data')
        
