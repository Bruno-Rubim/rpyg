from entity.model import Entity
from interface import UI
from atack.factory import AtackFactory 
from atack.model import Atack 
import random

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
        self.atacks = atacks
        self.base_defense = base_defense
        self.base_dodge = base_dodge
        self.battle = None
        super().__init__(name, actions, type, base_hp, elements)

    def battle_turn(self):
        if self.current_hp <= 0:
            UI.print_text(f"\n{self.name} has perished.\n")
            self.battle.over = True
            return

        actions = [*self.actions]
        choice = random.randint(0, len(actions) - 1)
        UI.print_text(f"\n{self.name} chose to {actions[choice]}\n")
        action = actions[choice]
        match action:
            case "run":
                self.player_ran = True
                UI.print_text(f"{self.name} flees from battle, like a coward\n")
            case "atack":
                self.attack_player()

    def attack_player(self):
        atacks = [*self.atacks]
        choice = random.randint(0, len(atacks) - 1)

        UI.print_text(f"""{self.name} uses "{atacks[choice]}"\n""")
        atack_name = atacks[choice]
        atack_object: Atack = AtackFactory.get_atack(name=atack_name, atacker=self, battle=self.battle)
        effect = atack_object.perform()
        self.battle.affect(self, effect)

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
