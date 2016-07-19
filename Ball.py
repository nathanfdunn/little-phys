from Util import Point, sgn

class Ball:
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy

    def move(self):
        self.x += sgn(self.vx)
        self.y += sgn(self.vy)

    def applyAcc(self, ax=0, ay=0):
        self.vx += ax
        self.vy += ay

    @property
    def pos(self):
        return Point(self.x, self.y)

    def __repr__(self):
        return 'pos=%s,%s vel=%s,%s;'%(self.x,self.y,self.vx,self.vy)
