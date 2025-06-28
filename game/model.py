from entity.player.model import Player
from json_importer import JsonImporter

class Game:
    instance = None
    initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def __init__(self, username = ''):
        if Game.initialized:
            return
        Game.initialized = True
        self.player = None
        
    def set_player(self, player_class_index):
        player_classes = JsonImporter.loadJSON('player')
        data_object = player_classes[player_class_index]
        self.player = Player(
            actions = data_object.get("actions", []),
            class_name = data_object.get("name", ''),
            atacks = data_object.get("atacks", []),
            base_hp = data_object.get("base_hp", 1),
            base_dodge = data_object.get("base_dodge", 0),
            base_defense = data_object.get("base_defense", 0),
        )
            
    def save(self):
        ...

