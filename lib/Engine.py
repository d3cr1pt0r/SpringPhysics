import sfml as sf

class Engine(object):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.game = None

        self.clock = sf.Clock()
        self.current_time = self.clock.elapsed_time.seconds
        self.dt = 0.01666666666666666666666666666667
        self.acc = 0.0
        self.t = 0.0

        self.init()

    def init(self):
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.height), self.title)

    def setGame(self, game):
        self.game = game

    def start(self):
        if self.game is None:
            print 'Game must be set with setGame first!'
            return

        self.game.start()

        while self.window.is_open:
            frame_time = self.clock.restart()
            self.acc += frame_time.seconds

            while self.acc > self.dt:
                self.checkEvents()
                self.update()

                self.acc -= self.dt
                self.t += self.dt

            self.render()

    def checkEvents(self):
        for event in self.window.events:
            if type(event) is sf.CloseEvent:
                self.window.close()

            self.game.events(event)

    def update(self):
        self.game.update(self.dt)

    def render(self):
        self.window.clear(sf.Color(20, 20, 20))
        self.game.render(self.window)
        self.window.display()