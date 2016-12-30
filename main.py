from Engine import Engine
from SpringsGame import SpringsGame

game = SpringsGame()

engine = Engine(800, 600, 'Springs')
engine.setGame(game)
engine.start()