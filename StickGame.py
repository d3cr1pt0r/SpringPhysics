import sfml as sf
from lib.Game import Game
from lib.Particle import VerletParticleContained
from lib.Stick import VerletStick

class StickGame(Game):
    def __init__(self):
        super(StickGame, self).__init__()

        self.points = []
        self.sticks = []

    def start(self):
        p1 = VerletParticleContained(position=sf.Vector2(100, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p2 = VerletParticleContained(position=sf.Vector2(180, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p3 = VerletParticleContained(position=sf.Vector2(100, 180), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p4 = VerletParticleContained(position=sf.Vector2(180, 180), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))

        p5 = VerletParticleContained(position=sf.Vector2(200, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p6 = VerletParticleContained(position=sf.Vector2(250, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p7 = VerletParticleContained(position=sf.Vector2(300, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))
        p8 = VerletParticleContained(position=sf.Vector2(350, 100), size=3, mass=1, bounce=0.8, friction=0.999, gravity=sf.Vector2(0, 0.1))

        p1.setWalls(0, 800, 0, 600)
        p2.setWalls(0, 800, 0, 600)
        p3.setWalls(0, 800, 0, 600)
        p4.setWalls(0, 800, 0, 600)
        p5.setWalls(0, 800, 0, 600)
        p6.setWalls(0, 800, 0, 600)
        p7.setWalls(0, 800, 0, 600)
        p8.setWalls(0, 800, 0, 600)

        p1.old_position = sf.Vector2(97, 100)
        p8.locked = True

        self.points.append(p1)
        self.points.append(p2)
        self.points.append(p3)
        self.points.append(p4)
        self.points.append(p5)
        self.points.append(p6)
        self.points.append(p7)
        self.points.append(p8)

        self.sticks.append(VerletStick(p1, p2))
        self.sticks.append(VerletStick(p2, p4))
        self.sticks.append(VerletStick(p4, p3))
        self.sticks.append(VerletStick(p3, p1))
        self.sticks.append(VerletStick(p1, p4))
        self.sticks.append(VerletStick(p2, p3))

        self.sticks.append(VerletStick(p8, p7))
        self.sticks.append(VerletStick(p7, p6))
        self.sticks.append(VerletStick(p5, p6))
        self.sticks.append(VerletStick(p2, p5))

    def events(self, event):
        if event == sf.MouseMoveEvent:
            self.points[7].position.x = event.position.x
            self.points[7].position.y = event.position.y

    def update(self, dt):
        for point in self.points:
            point.update(dt)
        for stick in self.sticks:
            stick.update(dt)

    def render(self, window):
        for stick in self.sticks:
            stick.render(window)
        for point in self.points:
            point.render(window)
