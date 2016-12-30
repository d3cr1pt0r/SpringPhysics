import sfml as sf
from Game import Game
from Particle import Particle, ParticleContained
from Spring import Spring

class SpringsGame(Game):

    def __init__(self):
        super(SpringsGame, self).__init__()
        self.width = 20
        self.height = 15

        self.particles = [[0 for y in range(self.height)] for x in range(self.width)]
        self.springs = []

    def getConnectableParticles(self, x, y):
        cp = []
        if x + 1 < self.width:
            cp.append(self.particles[x+1][y])
        if y + 1 < self.height:
            cp.append(self.particles[x][y+1])
        return cp

    def start(self):
        for y in range(self.height):
            for x in range(self.width):
                p = ParticleContained(sf.Vector2(50 + x * 20, 50 + y * 20), 3, 1, 1, sf.Vector2(0, 50))
                p.setWalls(0, 800, 0, 600)
                if y == 0 and (x == 0 or x == self.width - 1):
                    p.setLocked(True)
                self.particles[x][y] = p

        for y in range(self.height):
            for x in range(self.width):
                p1 = self.particles[x][y]
                cp = self.getConnectableParticles(x, y)
                for p in cp:
                    s = Spring(p1, p, 500, 10, 20)
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