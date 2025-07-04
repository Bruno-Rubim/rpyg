from abc import ABC, abstractmethod
from elements import element_efect, ElementResult
from typing import final
from entity.model import Entity

# Template
# Classe abstrata de ataque com uma sequência padrão de métodos que podem ser substituidas pelas classes que à herdam
class Atack(ABC):
    def __init__(self, 
            name: str,
            atacker: Entity, 
            battle,
            damage = 5, 
            element = '', 
            advantage_mult = 1.5, 
            disadvantage_mult = 0.75):
        self.atacker = atacker
        self.name = name
        self.damage = damage
        self.element = element
        self.advantage_mult = advantage_mult
        self.disadvantage_mult = disadvantage_mult
        self.battle = battle
        self.reciever: Entity = battle.get_oponent(atacker)
        
        self.final_damage = 0
        self.message = 0

    def calc_damage(self):
        result = 0
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                result = self.damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                result = self.damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                result = self.damage 
        result = int(result)
        self.final_damage = result

    def cause_effects(self):
        ...

    def write_message(self):
        self.message = str(self.final_damage) + ' damage to ' + self.reciever.name 
        if self.reciever.current_hp <= 0:
            self.message += ', ending its life.'

    @final
    def perform(self):
        self.calc_damage()
        self.cause_effects()
        self.write_message()
        return {
            'damage': self.final_damage,
            'message': self.message
        }

class Stab(Atack):
    def __init__(self, 
        atacker, 
        battle, 
        ):
        super().__init__(
            atacker = atacker,
            battle = battle,
            name = "stab",
            damage = 3,
            element = "ghost",
            advantage_mult = 1.3, 
            disadvantage_mult = 0.5)

    def calc_damage(self) -> int:
        final_damage = self.damage * self.atacker.base_dodge/3
        result = 0
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                result = final_damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                result = final_damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                result = final_damage
        result = int(result)
        self.final_damage = result

class FireBreath(Atack):
    def __init__(self, 
        atacker, 
        battle, 
        ):
        super().__init__(
            atacker = atacker, 
            battle = battle,
            name = "fire_breath", 
            damage = 7,
            element = "fire",
            advantage_mult = 1.7,
            disadvantage_mult = 0.2
        )

class Spit(Atack):
    def __init__(self, 
        atacker, 
        battle, 
        ):
        super().__init__(
            atacker = atacker, 
            battle = battle,
            name = "spit", 
            damage = 2,
            element = "water",
        )

class Shoot(Atack):
    def __init__(self, 
        atacker, 
        battle, 
        ):
        super().__init__(
            atacker = atacker, 
            battle = battle,
            name = "shoot", 
            damage = 5,
            element = "fire",
            advantage_mult = 2,
            disadvantage_mult = 0.1
        )

    def calc_damage(self) -> int:
        final_damage = self.damage / (self.reciever.base_dodge/3)
        result = 0
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                result = final_damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                result = final_damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                result = final_damage
        result = int(result)
        self.final_damage = result
    

class PunchHolder(Atack):
    def __init__(self, 
        atacker, 
        battle, 
        ):
        super().__init__(
            atacker = atacker, 
            battle = battle,
            name = "punchholder", 
            damage = 2,
            element = "normal",
            advantage_mult = 2,
            disadvantage_mult = 0.1
        )

    def calc_damage(self) -> int:
        final_damage = self.damage * (self.atacker.base_hp - self.atacker.current_hp)
        result = 0
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                result = final_damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                result = final_damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                result = final_damage
        result = int(result)
        self.final_damage = result