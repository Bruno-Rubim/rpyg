from entity.model import Entity

class Npc(Entity):
    def __init__(self, 
        name,
        actions,
        type,
        base_hp,
        elements,
        ):
        self.name = name
        self.type = type
        super().__init__(
            actions,
            base_hp,
            elements
        )

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
