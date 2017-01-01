import sfml as sf

class Point(object):

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

class PointContained(Point):

    def __init__(self, position, size, mass, friction, gravity):
        super(PointContained, self).__init__(position, size, mass, friction, gravity)

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
        super(PointContained, self).update(dt)
        self.containParticle()

    def containParticle(self):
        if self.position.x - self.size < self.left:
            self.position.x = self.left + self.size
            self.velocity.x *= -1
        if self.position.x + self.size > self.right:
            self.position.x = self.right - self.size
            self.velocity.x *= -1
        if self.position.y - self.size < self.top:
            self.position.y = self.top + self.size
            self.velocity.y *= -1
        if self.position.y + self.size > self.bottom:
            self.position.y = self.bottom - self.size
            self.velocity.y *= -1

class VerletPoint(Point):

    def __init__(self, position, size, mass, bounce, friction, gravity):
        self.position = position
        self.old_position = position
        self.size = size
        self.locked = False

        self.mass = mass
        self.bounce = bounce
        self.friction = friction
        self.gravity = gravity
        self.velocity = sf.Vector2(0, 0)

        super(VerletPoint, self).init()

    def update(self, dt):
        if not self.locked:
            self.velocity = (self.position - self.old_position) * self.friction
            self.old_position = sf.Vector2(self.position.x, self.position.y)
            self.position += self.velocity
            self.position += self.gravity

class VerletointContained(VerletPoint):

    def __init__(self, position, size, mass, bounce, friction, gravity):
        super(VerletointContained, self).__init__(position, size, mass, bounce, friction, gravity)

    def update(self, dt):
        super(VerletointContained, self).update(dt)
        self.containParticle()

    def setWalls(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def containParticle(self):
        if self.position.x + self.size > self.right:
            self.position.x = self.right - self.size
            self.old_position.x = self.position.x + self.velocity.x * self.bounce
        if self.position.x - self.size < self.left:
            self.position.x = self.left + self.size
            self.old_position.x = self.position.x + self.velocity.x * self.bounce
        if self.position.y + self.size > self.bottom:
            self.position.y = self.bottom - self.size
            self.old_position.y = self.position.y + self.velocity.y * self.bounce
        if self.position.y - self.size < self.top:
            self.position.y = self.top + self.size
            self.old_position.y = self.position.y + self.velocity.y * self.bounce