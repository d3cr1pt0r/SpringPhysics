import sfml as sf

from lib import Math
from lib.Game import Game
from lib.Point import VerletPointContained
from lib.Spring import VerletSpring

class VerletCloth(Game):

    def __init__(self):
        super(VerletCloth, self).__init__()

        self.width = 10
        self.height = 10

        self.points = [[0 for y in range(self.height)] for x in range(self.width)]
        self.springs = []

    def getConnectablePoints(self, x, y):
        cp = []
        if x + 1 < self.width:
            cp.append(self.points[x+1][y])
        if y + 1 < self.height:
            cp.append(self.points[x][y+1])
        if x + 1 < self.width and y + 1 < self.height:
            cp.append(self.points[x+1][y+1])
        if x - 1 >= 0 and y + 1 < self.height:
            cp.append(self.points[x-1][y+1])
        return cp

    def start(self):
        for y in range(self.height):
            for x in range(self.width):
                p = VerletPointContained(position=sf.Vector2(100 + x * 20, 100 + y * 20), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
                p.setWalls(0, 800, 0, 600)

                if y == 0:
                    p.setLocked(True)

                self.points[x][y] = p

        for y in range(self.height):
            for x in range(self.width):
                p1 = self.points[x][y]
                cp = self.getConnectablePoints(x, y)
                for p in cp:
                    s = VerletSpring(p1=p1, p2=p, stiffness=5, damping=5, length=Math.getDistance(p1.position, p.position))
                    self.springs.append(s)

    def update(self, dt):
        for spring in self.springs:
            spring.update(dt)

        for y in range(self.height):
            for x in range(self.width):
                self.points[x][y].update(dt)

    def render(self, window):
        for spring in self.springs:
            spring.render(window)

        for y in range(self.height):
            for x in range(self.width):
                self.points[x][y].render(window)
