import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.json')

class Data:
    def Write(self, data):
        with open(filename, "w") as write_file:
            json.dump(data, write_file)

    def Get(self):
        with open(filename, "r") as read_file:
            data = json.load(read_file)
            return data
