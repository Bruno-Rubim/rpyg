import json

class JsonImporter:
    def loadJSON(fileName: str):
        file = open(fileName + "/data.json").read()
        return json.loads(file)

    def findByName(list: list, name: str):
        for item in list:
            if (item['name'] == name):
                return item
        return None