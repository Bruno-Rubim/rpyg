from abc import ABC, abstractmethod
import random

# Strategy
# Abstrai uma família de algorítmos (estratégias) com
# funcionamentos intercambiáveis
# Elas herdam de uma interface abstrata que possúi o mesmo método
# que deve ser definido em cada subclasse 
# Elas são instanciadas pelo context (context.py)

class WeatherEffect(ABC):
    def __init__(self, battle, event_desc, efect_desc):
        self.battle = battle
        self.event_desc = event_desc
        self.efect_desc = efect_desc

    # método que deve ser implementado por toda subclasse
    @abstractmethod
    def affect(self, entities):
        pass
    
class Rain(WeatherEffect):
    def __init__(self, battle):
        event_desc = 'rain starts falling down the sky'
        efect_desc = 'the rain regenerates water creatures'
        super().__init__(battle, event_desc, efect_desc)

    def affect(self, entities):
        for entity in entities:
            if 'water' in entity.elements:
                entity.current_hp += 1

class Mist(WeatherEffect):
    def __init__(self, battle):
        event_desc = 'mist comes from the edges of your sight'
        efect_desc = 'the mist strengthens ghost creatures'
        super().__init__(battle, event_desc, efect_desc)

    def affect(self, entities):
        for entity in entities:
            if 'ghost' in entity.elements:
                entity.add_damage += 2

class Still(WeatherEffect):
    def __init__(self, battle):
        event_desc = 'the weather is still'
        efect_desc = 'normal creatures get stronger'
        super().__init__(battle, event_desc, efect_desc)

    def affect(self, entities):
        for entity in entities:
            if 'normal' in entity.elements:
                entity.add_damage += 1

# função para escolher estratégia em aleatório, não relacionada com
# o padrão de projeto
def get_rand_strat(battle) -> WeatherEffect:
    strat_list = [Rain(battle), Mist(battle), Still(battle)]
    r = random.randint(0, len(strat_list) - 1)
    return strat_list[r]