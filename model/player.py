class Player:
    def __init__(self, 
        name,
        actions,
        base_hp,
        base_defense,
        elements,
        status,
        dodge,
        attacks,
    ):
        self.name = name
        self.actions = actions
        self.attacks = attacks
        self.base_hp = base_hp
        self.dodge = dodge
        self.base_defense = base_defense
        self.elements = elements
        self.status = status