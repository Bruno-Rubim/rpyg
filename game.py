import sys
sys.dont_write_bytecode = True
from json_importer import JsonImporter
from player.model import Player
from battle.model import Battle
from input import requestNumberChoice
from npc.factory import NpcFactory

def selectPlayerClass() -> Player:
    print("""\nChose what your name will be:""")
    name = input("> ")
    print("""\nSelect your presence:""")
    player_class_amm = JsonImporter.loadJSON('player')
    for index, player_class in enumerate(player_class_amm):
        print(f"{index + 1} - {player_class['name']}")

    option = requestNumberChoice(1, len(player_class_amm)) - 1

    return Player(player_class_index=option, name=name)

selectPlayerClass()

min_t = NpcFactory.get_npc("mini_turret")

b = Battle(min_t)

b.battleLoop()