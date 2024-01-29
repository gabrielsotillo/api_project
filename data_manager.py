import json

class DataManager:

    def __init__(self):
        self.file = open('data.json', 'r') # Read a json file
        self.data = json.load(self.file) # Convert json file into a Python object (dict/list)
        self.file.close()

    def update_json(self):
        with open('data.json', 'w') as outfile:
            json.dump(self.data, outfile, indent=2)

    def check_id(self, id: int):
        for movie in self.data:
            if movie['id'] == id:
                return True
        return False