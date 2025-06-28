from entity.npc.model import Enemy
from entity.model import Entity

class Battle():
    def __init__(self, enemy: Enemy):
        from game.model import Game
        self.player = Game().player
        self.enemy = enemy

    def get_oponent(self, caller: Entity) -> Entity:
        from entity.player.model import Player
        if type(caller) is Enemy:
            return self.player
        elif type(caller) is Player:
            return self.enemy

    def atack():
        ...

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