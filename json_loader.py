from model.npc import NPC
import json

def jsonToList(fileName):
    file = open("JSON/" + fileName + ".json").read()
    return json.loads(file)

def findByName(list, name):
    for item in list:
        if (item['name'] == name):
            return item
    return 'nothin'

class JsonImporter:
    def __init__(self):
        self.npcs = jsonToList('npcs')

    def get_npc(self, name) -> NPC:
        data_object = findByName(self.npcs, name)
        npc = NPC(
            name = data_object.get('name'),
            actions = data_object.get('actions'),
            base_hp = data_object.get('base_hp'),
            dodge = data_object.get('dodge'),
            base_defense = data_object.get('base_defense'),
            attacks = data_object.get('attacks', None),
            elements = data_object.get('elements', []),
            status = data_object.get('status', []),
            )
        return npc