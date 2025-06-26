from abc import ABC, abstractmethod
from elements import element_efect, ElementResult

# Template
# Classe abstrata de ataque com uma sequência padrão de métodos
class Attack(ABC):
    def __init__(self, 
            attacker, 
            reciever, 
            damage = 5, 
            element = '', 
            advantage_mult = 1.5, 
            disadvantage_mult = 0.75):
        self.attacker = attacker
        self.reciever = reciever
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
    
    @abstractmethod
    def perform(self):

        print(f"{self.attacker} attacks {self.reciever}")