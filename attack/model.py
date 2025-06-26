from abc import ABC, abstractmethod
from elements import element_efect, ElementResult

# Template
# Classe abstrata de ataque com uma sequência padrão de métodos
class AttackFactory(ABC):
    def __init__(self, 
            name,
            attacker, 
            reciever, 
            damage = 5, 
            element = '', 
            advantage_mult = 1.5, 
            disadvantage_mult = 0.75):
        self.attacker = attacker
        self.reciever = reciever
        self.name = name
        self.damage = damage
        self.element = element
        self.advantage_mult = advantage_mult
        self.disadvantage_mult = disadvantage_mult

    def calc_damage(self):
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                return self.damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                return self.damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                return self.damage 
    
    def perform(self):
        damage = self.calc_damage()
        self.attacker.current_health -= damage
        print(f"{self.attacker} attacks {self.reciever}")

class Stab(Attack):
    def __init__(self, 
        attacker, 
        reciever, 
        ):
        super().__init__(
            attacker, 
            reciever, 
            "stab", 
             3,
             "ghost",
             1.3, 
             0.5)

    def calc_damage(self):
        final_damage = self.damage * self.attacker.base_dodge/3
        match(element_efect(self.element, self.reciever.elements[0])):
            case ElementResult.ADVANTAGE.value:
                return final_damage * self.advantage_mult
            case ElementResult.DISADVANTAGE.value:
                return final_damage * self.disadvantage_mult
            case ElementResult.NONE.value:
                return final_damage

""" 
        "fire_breath",
         7,
         "fire",
         1.7,
         0.2
 """