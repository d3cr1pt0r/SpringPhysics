import sfml as sf

from lib.Game import Game
from lib.Point import PointContained
from lib.Spring import Spring


class SpringsGame(Game):

    def __init__(self):
        super(SpringsGame, self).__init__()
        self.width = 10
        self.height = 10

        self.particles = [[0 for y in range(self.height)] for x in range(self.width)]
        self.springs = []

    def getConnectableParticles(self, x, y):
        cp = []
        if x + 1 < self.width:
            cp.append(self.particles[x+1][y])
        if y + 1 < self.height:
            cp.append(self.particles[x][y+1])
        if x + 1 < self.width and y + 1 < self.height:
            cp.append(self.particles[x+1][y+1])
        return cp

    def start(self):
        for y in range(self.height):
            for x in range(self.width):
                p = PointContained(sf.Vector2(100 + x * 20, 100 + y * 20 - x * 5), 3, 1, 1, sf.Vector2(0, 50))
                p.setWalls(0, 800, 0, 600)
                self.particles[x][y] = p

        for y in range(self.height):
            for x in range(self.width):
                p1 = self.particles[x][y]
                cp = self.getConnectableParticles(x, y)
                for p in cp:
                    s = Spring(p1, p, 1000, 20, 20)
                    self.springs.append(s)

    def update(self, dt):
        for spring in self.springs:
            spring.update(dt)
        for y in range(self.height):
            for x in range(self.width):
                self.particles[x][y].update(dt)

    def render(self, window):
        for spring in self.springs:
            spring.render(window)
        for y in range(self.height):
            for x in range(self.width):
                self.particles[x][y].render(window)