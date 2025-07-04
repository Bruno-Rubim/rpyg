from abc import ABC, abstractmethod

class WeatherEffect(ABC):
    def __init__(self, battle):
        self.battle = battle

    @abstractmethod
    def affect(self, entities):
        pass
    
class Rain(WeatherEffect):
    def affect(self, entities):
        for entity in entities:
            if entity.elements.contains('water'):
                entity.current_hp += 1

class Mist(WeatherEffect):
    def affect(self, entities):
        for entity in entities:
            if entity.elements.contains('ghost'):
                entity.add_damage += 1
