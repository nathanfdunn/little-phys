from Util import Point

class Air:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.char = ' '

    @property
    def pos(self):
        return Point(self.x, self.y)

    isYielding = True

    kind = 'air'