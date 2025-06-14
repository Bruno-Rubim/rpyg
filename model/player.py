class Player:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self,
        name,
        actions,
        base_hp,
        base_defense,
        elements,
        status,
        base_dodge,
        attacks,
    ):
        self.name = name
        self.actions = actions
        self.attacks = attacks
        self.base_hp = base_hp
        self.base_dodge = base_dodge
        self.base_defense = base_defense
        self.elements = elements
        self.status = status