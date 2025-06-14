from npc.model import Npc
from npc.factory import NpcFactory
import json

def loadJSON(fileName):
    file = open("JSON/" + fileName + ".json").read()
    return json.loads(file)

def findByName(list, name):
    for item in list:
        if (item['name'] == name):
            return item
    return None

class JsonImporter:
    def __init__(self):
        self.npcs = loadJSON('npcs')

    def get_npc(self, name) -> Npc:
        data_object = findByName(self.npcs, name)
        npc = NpcFactory.getNpc(data_object)
        return npc