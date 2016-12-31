import sfml as sf

from lib.Game import Game
from lib.Particle import VerletParticleContained
from lib.Spring import VerletSpring

class VerletTest(Game):

    def __init__(self):
        super(VerletTest, self).__init__()

        self.points = []
        self.springs = []

    def start(self):
        self.p1 = VerletParticleContained(position=sf.Vector2(100, 100), size=5, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        self.p2 = VerletParticleContained(position=sf.Vector2(200, 100), size=5, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        self.p3 = VerletParticleContained(position=sf.Vector2(150, 50), size=5, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))

        self.p1.setWalls(0, 800, 0, 600)
        self.p2.setWalls(0, 800, 0, 600)
        self.p3.setWalls(0, 800, 0, 600)

        self.points.append(self.p1)
        self.points.append(self.p2)
        self.points.append(self.p3)

        self.springs.append(VerletSpring(self.p1, self.p2, 5, 1, 50))
        self.springs.append(VerletSpring(self.p2, self.p3, 5, 1, 50))
        self.springs.append(VerletSpring(self.p3, self.p1, 5, 1, 50))

    def update(self, dt):
        for spring in self.springs:
            spring.update(dt)

        for point in self.points:
            point.update(dt)

    def render(self, window):
        for spring in self.springs:
            spring.render(window)

        for point in self.points:
            point.render(window)
