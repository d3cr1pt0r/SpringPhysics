import sfml as sf

from lib import Math


class Spring(object):

    def __init__(self, p1, p2, stiffness, damping, length):
        self.p1 = p1
        self.p2 = p2
        self.stiffness = stiffness
        self.damping = damping
        self.length = length
        self.force = sf.Vector2(0, 0)

        self.renderShape = sf.VertexArray(sf.PrimitiveType.LINES, 2)

    def applyStringPhysics(self, dt):
        p1_p2 = self.p2.position - self.p1.position
        v1 = self.p1.velocity - self.p2.velocity
        v2 = self.p2.velocity - self.p1.velocity

        self.force = Math.getNormalized(p1_p2) * (Math.getLength(p1_p2) - self.length) * self.stiffness
        f1 = self.force - (v1 * self.damping)
        f2 = self.force + (v2 * self.damping)

        f1.x /= self.p1.mass
        f1.y /= self.p1.mass
        f2.x /= self.p1.mass
        f2.y /= self.p1.mass

        self.p1.velocity += f1 * dt
        self.p2.velocity -= f2 * dt

    def update(self, dt):
        self.applyStringPhysics(dt)

    def render(self, window):
        self.renderShape[0].position = self.p1.position
        self.renderShape[1].position = self.p2.position

        window.draw(self.renderShape)

class VerletSpring(Spring):

    def __init__(self, p1, p2, stiffness, damping, length):
        super(VerletSpring, self).__init__(p1, p2, stiffness, damping, length)

    def applyStringPhysics(self, dt):
        p1_p2 = self.p2.position - self.p1.position
        v1 = self.p1.velocity - self.p2.velocity
        v2 = self.p2.velocity - self.p1.velocity

        self.force = Math.getNormalized(p1_p2) * (Math.getLength(p1_p2) - self.length) * self.stiffness
        f1 = self.force - (v1 * self.damping)
        f2 = self.force + (v2 * self.damping)

        f1.x /= self.p1.mass
        f1.y /= self.p1.mass
        f2.x /= self.p1.mass
        f2.y /= self.p1.mass

        if not self.p1.locked:
            self.p1.position += f1 * dt
        if not self.p2.locked:
            self.p2.position -= f2 * dt