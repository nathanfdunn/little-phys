from Util import sgn, DEFAULT_DIMENSION, Point
from Barrier import Barrier
from Water import WaterElement
from Air import Air
from Deflector import Deflector

class Board:
    def __init__(self, balls=None, barriers=None, deflectors=None, water=None, dim=None, verbose=False):
        self.balls = balls or []
        self.dim = dim or DEFAULT_DIMENSION
        self.barriers = barriers or []
        self.water = water or []
        self.history = []
        self.recordPositions()
        self.verbose = verbose
        self.deflectors = deflectors or []

    def recordPositions(self):
        self.history.extend(ball.pos for ball in self.balls)

    def getItemAt(self, x, y=None):
        if y is None:
            x, y = x
        for obj in self.water + self.barriers + self.deflectors:
            if obj.pos == Point(x,y):
                return obj
        return Air(x,y)

    def applyGravity(self):
        for ball in self.balls:
            there = self.getItemAt(ball.pos)
            below = self.getItemAt(ball.pos.x, ball.pos.y-1)
            if there.kind == 'air' and below.isYielding:
                ball.vy -= 1

    def update(self):
        for ball in self.balls:
            ball.move()

        self.resolveCollisions()
        self.recordPositions()

        self.applyGravity()
        if self.verbose:
            print(self.balls, '\n\n')

    def resolveCollisions(self):
        for ball in self.balls:
            for barrier in self.barriers:
                if ball.pos == barrier.pos:
                    barrier.bounceBall(ball)

        for ball in self.balls:
            for waterElement in self.water:
                if ball.pos == waterElement.pos:
                    waterElement.bouyBall(ball)

        for ball in self.balls:
            for deflector in self.deflectors:
                if ball.pos == deflector.pos:
                    deflector.deflectBall(ball)

    def getArrayRepr(self):
        out = [[None]*self.dim.width for i in range(self.dim.height)]
        for waterElement in self.water:
            if self.isOnBoard(waterElement):
                out[(self.dim.height-1)-waterElement.y][waterElement.x] = waterElement.icon
        for barrier in self.barriers:
            if self.isOnBoard(barrier):
                out[(self.dim.height-1)-barrier.y][barrier.x] = barrier.char

        for deflector in self.deflectors:
            if self.isOnBoard(deflector):
                out[(self.dim.height-1)-deflector.y][deflector.x] = deflector.dir

        for ball in self.balls:
            if self.isOnBoard(ball):
                out[(self.dim.height-1)-ball.y][ball.x] = 'O'
        return out

    def isOnBoard(self, obj):
        return 0 <= obj.x < self.dim.width and 0 <= obj.y < self.dim.height

    def __str__(self):
        array = self.getArrayRepr()
        out = ''
        block = ''
        out += block*(len(array[0]) + 2) + '\n'
        for row in array:
            out += block
            for el in row:
                out += el if el is not None else ' '
            out += block
            out += '\n'
        out += block*(len(array[0]) + 2)
        return out
