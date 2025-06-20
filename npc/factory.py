from npc.model import Npc, Enemy, Friend
from json_importer import JsonImporter

class NpcFactory:
    npc_list = JsonImporter.loadJSON('npc')

    def get_npc(name: str) -> Npc:
        data_object = JsonImporter.findByName(name)
        match data_object.get('type'):
            case 'enemy':
                print('this is an enemy')
                npc = Enemy(
                        name = data_object.get('name'),
                        type = data_object.get('type'),
                        actions = data_object.get('actions'),
                        base_hp = data_object.get('base_hp'),
                        base_dodge = data_object.get('base_dodge'),
                        base_defense = data_object.get('base_defense'),
                        attacks = data_object.get('attacks', None),
                        elements = data_object.get('elements', []),
                        )
                return npc
            case 'friend':
                print('this is a friend')
                npc = Friend(
                        name = data_object.get('name'),
                        type = data_object.get('type'),
                        actions = data_object.get('actions'),
                        base_hp = data_object.get('base_hp'),
                        elements = data_object.get('elements', []),
                        dialogue = data_object.get('dialogue', ['no_d'])
                        )
                return npc