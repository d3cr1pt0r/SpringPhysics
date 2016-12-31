from SpringsGame import SpringsGame
from VerletTest import VerletTest
from lib.Engine import Engine

game = SpringsGame()
game = VerletTest()

engine = Engine(800, 600, 'Springs')
engine.setGame(game)
engine.start()