import json

class JsonImporter:
    def load_json(file_path: str):
        file = open(file_path + "/data.json").read()
        return json.loads(file)

    def findByName(list: list, name: str):
        for item in list:
            if (item['name'] == name):
                return item
        return None