import sfml as sf
import Math

class VerletStick(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.distance = Math.getDistance(p1.position, p2.position)

        self.renderShape = sf.VertexArray(sf.PrimitiveType.LINES, 2)

    def update(self, dt):
        for i in range(5):
            d = self.p2.position - self.p1.position
            current_dist = Math.getDistance(self.p1.position, self.p2.position)
            diff = self.distance - current_dist
            p = (diff / current_dist) / 2.0
            offset = d * p

            if not self.p1.locked:
                self.p1.position -= offset
            if not self.p2.locked:
                self.p2.position += offset

            self.p1.containParticle()
            self.p2.containParticle()

    def render(self, window):
        self.renderShape[0].position = self.p1.position
        self.renderShape[1].position = self.p2.position

        window.draw(self.renderShape)