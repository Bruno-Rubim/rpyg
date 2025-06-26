from player.model import Player
from input import requestNumberChoice
from npc.model import Enemy
from json_importer import JsonImporter
from attack.factory import AttackFactory
import random

attacks = JsonImporter.loadJSON('attack')

class Battle():
    def __init__(self, enemy: Enemy):
        self.enemy = enemy
        self.player_ran = False
        self.enemy_ran = False
        self.ended = False
        self.player = Player(0, "")

    def playerBattleAction(self):
        
        print(f"\nWhat do you do, {self.player.name}?\n")
        
        actions = [*self.player.actions]
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
            case "attack":
                attack = JsonImporter.findByName(attacks, self.player.attacks[0])

                print(f"You attacked {self.enemy.name} with {attack['name']}\n")

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
            case "attack":
                attacks = self.enemy.attacks
                attack_name = attacks[random.randint(0, len(attacks) - 1)]

                print(f"{self.enemy.name} attacked you with {attack['name']}\n")

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