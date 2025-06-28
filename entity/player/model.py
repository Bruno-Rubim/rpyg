from entity.model import Entity

class Player(Entity):
    def __init__(self,
        actions,
        base_hp,
        class_name,
        atacks,
        base_dodge,
        base_defense,
        ):

        self.class_name = class_name
        self.atacks = atacks
        self.base_dodge = base_dodge
        self.base_defense = base_defense
        self.status = []
        super().__init__(
            actions,
            base_hp,
        )