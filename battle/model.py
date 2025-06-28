from game.model import Game
from input import requestNumberChoice
from entity.npc.model import Enemy
import randome

class Battle():
    def __init__(self, enemy: Enemy):
        self.player = Game()
        self.enemy = enemy

    # def playerBattleAction(self):
        
    #     print(f"\nWhat do you do, {self.player.name}?\n")
        
    #     actions = [*self.player.actions]
    #     #actions.insert(0, "end turn")
    #     options = ""

    #     for i in range(0, len(actions)):
    #         options += f"{i}) {actions[i]}  "

    #     print(f"Options:\n{options}")

    #     choice = requestNumberChoice(0, len(actions) - 1)
    #     print(f"You chose to {actions[choice]}\n")
    #     return actions[choice]

    # def playerBattleTurn(self):
    #     action = self.playerBattleAction()
    #     match action:
    #         case "run":
    #             self.player_ran = True
    #             print("You flee from battle, like a coward\n")
    #         case "atack":
    #             atack = atackFactory.get_atack(name=self.player.atacks[0], atacker=self.player, reciever=self.enemy)
    #             message = atack.perform()
    #             print(f"You atacked {self.enemy.name} with {atack.name}\nDealing {message}\n")

    # def enemyBattleAction(self):
    #     actions = self.enemy.actions
    #     choice = actions[random.randint(0, len(actions) - 1)]
    #     print(f"{self.enemy.name} chose to {choice}\n")
    #     return choice

    # def enemyBattleTurn(self):
    #     action = self.enemyBattleAction()
    #     match action:
    #         case "run":
    #             self.enemy_ran = True
    #             print(f"{self.enemy.name} flees from battle, like a coward\n")
    #         case "atack":
    #             atacks = self.enemy.atacks
    #             atack_name = atacks[random.randint(0, len(atacks) - 1)]
    #             atack = atackFactory.get_atack(name=atack_name, atacker=self.enemy, reciever=self.player)
    #             message = atack.perform()
    #             print(f"{self.enemy.name} atacked you with {atack.name}\nDealing {message}\n")

    # def print_stats(self, whos):
    #     if whos == 'player':
    #         print(f"You're at {self.player.current_hp} health")
    #     else:
    #         print(f"{self.enemy.name} is at {self.enemy.current_hp} health")

    # def checkState(self):
    #     if (
    #         self.player_ran or
    #         self.enemy_ran or
    #         Player(0, "").current_hp <= 0 or
    #         self.enemy.current_hp <= 0 
    #         ):
    #         print("The battle is over.\n")
    #         self.ended = True
    #     pass

    # def do_turn(self, whos):
    #     if whos == 'player':
    #         self.playerBattleTurn()
    #         self.print_stats('enemy')
    #     else:
    #         self.enemyBattleTurn()
    #         self.print_stats('player')
    #     self.checkState()

    # def battleLoop(self):
        while (True):
            self.do_turn('player')
            if self.ended:
                break
            self.do_turn('enemy')
            if self.ended:
                break