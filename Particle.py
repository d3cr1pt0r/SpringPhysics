import sfml as sf

class Particle(object):

    def __init__(self, position, size, mass, friction, gravity):
        self.position = position
        self.size = size
        self.mass = mass
        self.friction = friction
        self.locked = False

        self.gravity = gravity
        self.accelaration = sf.Vector2(0, 0)
        self.velocity = sf.Vector2(0, 0)

        self.init()

    def init(self):
        self.renderShape = sf.CircleShape()
        self.renderShape.radius = self.size
        self.renderShape.fill_color = sf.Color.WHITE
        self.renderShape.origin = ((self.size*2) / 2, (self.size*2) / 2)

    def setLocked(self, locked):
        self.locked = locked

    def update(self, dt):
        #self.velocity *= self.friction

        if not self.locked:
            self.velocity += self.accelaration * dt
            self.velocity += self.gravity * dt
            self.position += self.velocity * dt

    def render(self, window):
        self.renderShape.position = self.position
        window.draw(self.renderShape)

class ParticleContained(Particle):

    def __init__(self, position, size, mass, friction, gravity):
        super(ParticleContained, self).__init__(position, size, mass, friction, gravity)

        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

    def setWalls(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def update(self, dt):
        super(ParticleContained, self).update(dt)
        self.containParticle()

    def containParticle(self):
        if self.position.x < self.left:
            self.position.x = self.left
            self.velocity.x *= -1
        if self.position.x > self.right:
            self.position.x = self.right
            self.velocity.x *= -1
        if self.position.y < self.top:
            self.position.y = self.top
            self.velocity.y *= -1
        if self.position.y > self.bottom:
            self.position.y = self.bottom
            self.velocity.y *= -1