from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self,
        actions,
        base_hp,
        elements: list
        ):
        self.actions = actions
        self.base_hp = base_hp
        self.current_hp = base_hp
        self.elements = elements