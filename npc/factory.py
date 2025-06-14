from npc.model import Npc, Enemy, Friend

class NpcFactory:
    def getNpc(data_object) -> Npc:
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