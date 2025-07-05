from json_importer import JsonImporter
from interface import UI
from entity.player.model import Player
from entity.npc.factory import NpcFactory
from entity.npc.model import Enemy
from entity.model import Entity
from battle.model import Battle
from weather.context import WeatherContext
from weather.strategies import get_rand_strat
import random

# Singleton
# Abstrai o gerenciamento de uma instância única e consistência de estado

class Game:
    instance = None
    initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
        # se quando instanciar a classe não houver uma insância salva
        # a classe cria uma nova e salva em uma variável da classe
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance
        # caso contrário ela retorna a mesma instância

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

    def print_stats(self, target: Entity):
        UI.print_text(f"\n{target.name} is at {target.current_hp} hp")

    def do_weather_efect(self, weather_context: WeatherContext, battle: Battle):
        self.rand_weather_strat(weather_context, battle)
        entities = battle.get_entities()
        weather_context.do_strat(entities)

    def rand_weather_strat(self, weather_context: WeatherContext, battle):
        r = random.randint(0, 1)
        if r == 0:
            weather_context.set_strat(get_rand_strat(battle))

    def battle_turn(self, battle, enemy: Enemy, weather_effect):
        if battle.over :
            return
        else:
            self.print_stats(self.player)
            self.player.add_damage = 0
            self.do_weather_efect(weather_effect, battle)
            self.player.battle_turn()
        if battle.over :
            return
        else:
            self.print_stats(enemy)
            enemy.add_damage = 0
            self.do_weather_efect(weather_effect, battle)
            enemy.battle_turn()

    def start_battle(self, enemy_name : str):
        enemy = NpcFactory.get_npc(enemy_name)
        weather_context = WeatherContext()
        battle = Battle(enemy)
        self.player.battle = battle
        enemy.battle = battle
        UI.print_text(f"\nA {enemy.name} challenges you")
        while not battle.over:
            self.battle_turn(battle, enemy, weather_context)

    def start(self):
        self.set_new_player()
        self.start_battle('chertzer')