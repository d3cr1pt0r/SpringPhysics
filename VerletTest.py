import sfml as sf

from lib.Game import Game
from lib.Particle import VerletParticleContained

class VerletTest(Game):

    def __init__(self):
        super(VerletTest, self).__init__()

    def start(self):
        self.p1 = VerletParticleContained(sf.Vector2(100, 100), 5, 0.8, 0.999, sf.Vector2(0, 0.1))
        self.p1.old_position = sf.Vector2(95, 99)
        self.p1.setWalls(0, 800, 0, 600)

    def update(self, dt):
        self.p1.update(dt)

    def render(self, window):
        self.p1.render(window)