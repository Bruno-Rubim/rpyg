from entity.npc.model import Npc, Enemy, Friend
from json_importer import JsonImporter

npc_list = JsonImporter.load_json('entity/npc')

class NpcFactory:

    def get_npc(name: str) -> Npc:
        data_object = JsonImporter.findByName(npc_list, name)
        match data_object.get('type'):
            case 'enemy':
                npc = Enemy(
                        name = data_object.get('name'),
                        type = data_object.get('type'),
                        actions = data_object.get('actions'),
                        base_hp = data_object.get('base_hp'),
                        base_dodge = data_object.get('base_dodge'),
                        base_defense = data_object.get('base_defense'),
                        atacks = data_object.get('atacks', None),
                        elements = data_object.get('elements', []),
                        )
                return npc
            case 'friend':
                npc = Friend(
                        name = data_object.get('name'),
                        type = data_object.get('type'),
                        actions = data_object.get('actions'),
                        base_hp = data_object.get('base_hp'),
                        elements = data_object.get('elements', []),
                        dialogue = data_object.get('dialogue', ['no_d'])
                        )
                return npc