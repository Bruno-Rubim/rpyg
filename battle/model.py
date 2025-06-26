from player.model import Player
from input import requestNumberChoice
from npc.model import Enemy
import random

class Battle():
    def __init__(self, enemy: Enemy):
        self.enemy = enemy
        self.player_ran = False
        self.enemy_ran = False
        self.ended = False

    def playerBattleAction(self):
        player = Player(0, "")
        
        print(f"\nWhat do you do, {player.name}?\n")
        
        actions = [*player.actions]
        #actions.insert(0, "end turn")
        options = ""

        for i in range(0, len(actions)):
            options += f"{i}) {actions[i]}  "

        print(f"Options:\n{options}")
        choice = requestNumberChoice(0, len(actions) - 1)
        print(f"You chose to {actions[choice]}\n")
        return actions[choice]

    def playerBattleTurn(self):
        action = self.playerBattleAction()
        match action:
            case "run":
                self.player_ran = True
                print("You flee from battle, like a coward\n")

    def enemyBattleAction(self):
        actions = self.enemy.actions
        choice = actions[random.randint(0, len(actions) - 1)]
        print(f"{self.enemy.name} chose to {choice}\n")
        return choice

    def enemyBattleTurn(self):
        action = self.enemyBattleAction()
        match action:
            case "run":
                self.enemy_ran = True
                print(f"{self.enemy.name} flees from battle, like a coward\n")

    def checkState(self):
        if (
            self.player_ran or
            self.enemy_ran or
            Player(0, "").current_hp <= 0 or
            self.enemy.current_hp <= 0 
            ):
            print("The battle is over.\n")
            self.ended = True
        pass

    def battleLoop(self):
        while (True):
            self.playerBattleTurn()
            self.checkState()
            if self.ended:
                break
            self.enemyBattleTurn()
            self.checkState()
            if self.ended:
                break