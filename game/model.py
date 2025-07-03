from json_importer import JsonImporter
from interface import UI
from entity.player.model import Player
from entity.npc.factory import NpcFactory
from entity.npc.model import Enemy
from battle.model import Battle

class Game:
    instance = None
    initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if Game.initialized:
            return
        Game.initialized = True
        self.player = None
        self.username = None
        
    def set_player_object(self, player_class_index):
        player_classes = JsonImporter.load_json('entity/player')
        data_object = player_classes[player_class_index]
        self.player = Player(
            actions = data_object.get("actions", []),
            class_name = data_object.get("name", ''),
            atacks = data_object.get("atacks", []),
            base_hp = data_object.get("base_hp", 1),
            base_dodge = data_object.get("base_dodge", 0),
            base_defense = data_object.get("base_defense", 0),
            elements = data_object.get("elements", []),
        )
    
    def set_new_player(self):
        self.username = UI.promt_user("""\nChose what your name will be:""")
        UI.print_text("""\nSelect your presence:""")
        player_classes = JsonImporter.load_json('entity/player')

        for index, player_class in enumerate(player_classes):
            UI.print_text(f"{index + 1} - {player_class['name']}")
        
        option = UI.request_number_choice(1, len(player_classes))
        self.set_player_object(option - 1)
        UI.print_text(f"""You chose "{self.player.class_name}".\nInteresting... """)

    def battle_turn(self, battle, enemy: Enemy):
        if battle.over :
            return
        else:
            self.player.battle_turn()
        if battle.over :
            return
        else:
            enemy.battle_turn()

    def start_battle(self, enemy_name : str):
        enemy = NpcFactory.get_npc(enemy_name)
        battle = Battle(enemy)
        self.player.battle = battle
        enemy.battle = battle
        UI.print_text(f"\nA {enemy.name} challenges you")
        while not battle.over:
            self.battle_turn(battle, enemy)

    def start(self):
        self.set_new_player()
        self.start_battle('mini_turret')

    def save(self):
        ...

