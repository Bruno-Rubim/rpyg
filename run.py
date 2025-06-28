import sys
sys.dont_write_bytecode = True
from game.model import Game

game = Game()

game.start()