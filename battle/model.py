from entity.npc.model import Enemy
from entity.model import Entity
from interface import UI

class Battle():
    def __init__(self, enemy: Enemy):
        from game.model import Game
        self.player = Game().player
        self.enemy = enemy
        self.flee = False
        self.over = False

    def affect(self, inflictor, effect):
        if inflictor is self.player:
            self.enemy.current_hp -= effect['damage']
            UI.print_text(effect['message'])
        if inflictor is self.enemy:
            self.enemy.current_hp -= effect['damage']
            UI.print_text(effect['message'])

    def get_oponent(self, caller: Entity) -> Entity:
        from entity.player.model import Player
        if type(caller) is Enemy:
            return self.player
        elif type(caller) is Player:
            return self.enemy