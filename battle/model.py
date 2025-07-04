from entity.npc.model import Enemy
from entity.model import Entity
from interface import UI
from weather.context import WeatherContext
from weather.strategies import get_rand_strat

# Mediator
# Abstrai a comunicação direta entre objetos
# Possúi um metodo para receber informações de objetos que é usada para afetar os demais

class Battle():
    def __init__(self, enemy: Enemy):
        from game.model import Game
        self.player = Game().player
        self.enemy = enemy
        self.flee = False
        self.over = False

    # método que recebe um objeto e sua ação, e utiliza essas informações para afetar os demais
    def affect(self, inflictor, effect):
        if inflictor is self.player:
            self.enemy.current_hp -= effect['damage']
            UI.print_text(effect['message'])
        if inflictor is self.enemy:
            self.player.current_hp -= effect['damage']
            UI.print_text(effect['message'])

    def get_oponent(self, caller: Entity) -> Entity:
        from entity.player.model import Player
        if type(caller) is Enemy:
            return self.player
        elif type(caller) is Player:
            return self.enemy
        
    def get_entities(self) -> list[Entity]:
        return [self.player, self.enemy]