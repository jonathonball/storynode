import pathlib
import os

class Finder:

    def getFileByExtension(self, path, file, ext):
        files = os.scandir(path)
        for file in files:
            print(file)
