from entity.model import Entity
from interface import UI
from atack.factory import AtackFactory
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from battle.model import Battle
    from atack.model import Atack

class Player(Entity):
    def __init__(self,
        actions,
        base_hp,
        class_name,
        atacks,
        base_dodge,
        base_defense,
        elements,
        ):

        self.name = class_name
        self.class_name = class_name
        self.atacks = atacks
        self.base_dodge = base_dodge
        self.base_defense = base_defense
        self.status = []
        self.battle: Battle = None
        self.add_damage = 0
        super().__init__(
            actions,
            base_hp,
            elements,
        )
    
    def battle_turn(self):
        if self.current_hp < 1:
            UI.print_text(f"\nYou have perished.\n")
            self.battle.over = True
            return

        UI.print_text(f"\nWhat do you do?\n")
        actions = [*self.actions]
        options = ""

        for i in range(0, len(actions)):
            options += f"{i}) {actions[i]}  "

        UI.print_text(f"Options:\n{options}")

        choice = UI.promt_user('', True, 0, len(actions) - 1)
        UI.print_text(f"You chose to {actions[choice]}\n")
        action = actions[choice]
        match action:
            case "run":
                self.battle.flee = True
                UI.print_text("You flee from battle, like a coward\n")
                self.battle.over = True
            case "atack":
                self.attack_enemy()

    def attack_enemy(self):
        UI.print_text(f"Choose your attack\n")
        atacks = [*self.atacks]
        options = ""

        for i in range(0, len(atacks)):
            options += f"{i + 1}) {atacks[i]}  "

        UI.print_text(options)
        choice = UI.promt_user('', True, 1, len(atacks))
        choice -= 1 
        UI.print_text(f"""You use "{atacks[choice]}"\n""")
        atack_name = atacks[choice]
        atack_object: Atack = AtackFactory.get_atack(name=atack_name, atacker=self, battle=self.battle)
        effect = atack_object.perform()
        self.battle.affect(self, effect)
