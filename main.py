from SpringsGame import SpringsGame
from VerletTest import VerletTest
from VerletCloth import VerletCloth
from StickGame import StickGame
from lib.Engine import Engine

game = SpringsGame()
game = VerletTest()
game = VerletCloth()
game = StickGame()

engine = Engine(800, 600, 'Springs')
engine.setGame(game)
engine.start()