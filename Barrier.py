from Util import Point, sgn

class Barrier:
    def __init__(self, x, y, normals):
        self.x=x
        self.y=y
        self.normals = normals
        self.char = '#'

    def bounceBall(self, ball):
        if '-' in self.normals:
            ball.y -= sgn(ball.vy)
            ball.vy = -ball.vy + sgn(ball.vy)

        if '|' in self.normals:
            ball.x -= sgn(ball.vx)
            ball.vx = -ball.vx + sgn(ball.vx)

    @property
    def pos(self):
        return Point(self.x, self.y)

    isYielding = False
    kind = 'barrier'
