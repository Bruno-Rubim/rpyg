from enum import Enum

class ElementResult(Enum):
    NONE = 0
    ADVANTAGE = 1
    DISADVANTAGE = 2

class Element:
    def __init__(self, advantages = [], disadvantages = []):
        self.advantages = advantages
        self.disadvantages = disadvantages

elements = {
    "water": Element(['fire'], ['ice']),
    "ice": Element(['water'], ['fire']),
    "fire": Element(['ice'], ['water']),
    "ghost": Element([], []),
    "normal": Element([], ['normal']),
}

def element_efect(dealer: str, reciever: str) -> int:
    if reciever in elements[dealer].advantages:
        return ElementResult.ADVANTAGE.value
    elif reciever in elements[dealer].disadvantages:
        return ElementResult.DISADVANTAGE.value
    else:
        return ElementResult.NONE.value