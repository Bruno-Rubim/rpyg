from abc import ABC

class Npc(ABC):
    def __init__(self, 
        name,
        type,
        actions,
        base_hp,
        elements,
        ):
        self.name = name
        self.type = type
        self.actions = actions
        self.base_hp = base_hp
        self.current_hp = base_hp
        self.elements = elements

class Enemy(Npc):
    def __init__(self,
        name,
        type,
        actions,
        base_hp,
        elements,
        atacks,
        base_defense,
        base_dodge,
        ):
        super().__init__(name, type, actions, base_hp, elements)
        self.atacks = atacks
        self.base_defense = base_defense
        self.base_dodge = base_dodge

class Friend(Npc):
    def __init__(self,
        name,
        type,
        actions,
        base_hp,
        elements,
        dialogue,
        ):
        super().__init__(name, type, actions, base_hp, elements)
        self.dialogue = dialogue
