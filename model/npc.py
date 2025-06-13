class NPC:
    def __init__(self, 
        name,
        actions,
        base_hp,
        dodge,
        base_defense,
        attacks,
        elements,
        status
        ):
        self.name = name
        self.actions = actions
        self.attacks = attacks
        self.base_hp = base_hp
        self.dodge = dodge
        self.base_defense = base_defense
        self.elements = elements
        self.status = status