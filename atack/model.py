from abc import ABC, abstractmethod
from elements import element_efect, ElementResult

# Template
# Classe abstrata de ataque com uma sequência padrão de métodos que podem ser substituidas pelas classes que à herdam
class Atack(ABC):
    def __init__(self, 
            name: str,
            atacker, 
            reciever, 
            damage = 5, 
            element = '', 
            advantage_mult = 1.5, 
            disadvantage_mult = 0.75):
        self.atacker = atacker
        self.reciever = reciever
        self.name = name
        self.damage = damage
        self.element = element
        self.advantage_mult = advantage_mult
        self.disadvantage_mult = disadvantage_mult

    def calc_damage(self) -> int:
        result = 0
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                result = self.damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                result = self.damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                result = self.damage 
        result = int(result)
        return result
    
    def perform(self) -> str:
        damage = self.calc_damage()
        self.reciever.current_hp -= damage
        return_msg = str(damage) + ' damage'
        if self.reciever.current_hp <= 0:
            return_msg += ', ending its life.'
        return return_msg

class Stab(Atack):
    def __init__(self, 
        atacker, 
        reciever, 
        ):
        super().__init__(
            atacker = atacker,
            reciever = reciever, 
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
        return result

class FireBreath(Atack):
    def __init__(self, 
        atacker, 
        reciever, 
        ):
        super().__init__(
            atacker = atacker, 
            reciever = reciever, 
            name = "fire_breath", 
            damage = 7,
            element = "fire",
            advantage_mult = 1.7,
            disadvantage_mult = 0.2
        )

class Shoot(Atack):
    def __init__(self, 
        atacker, 
        reciever, 
        ):
        super().__init__(
            atacker = atacker, 
            reciever = reciever, 
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
        return result