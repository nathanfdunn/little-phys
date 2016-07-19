from Util import Point, sgn

class WaterElement:
	def __init__(self, x, y, surface):
		self.x = x
		self.y = y
		self.depth = surface - self.y
		self.isYielding = self.depth == 0 # only surface is yielding
		self.icon = '~' if self.depth == 0 else ' '

	# Don't worry about horizontal for now...
	def bouyBall(self, ball):
		ball.vy -= sgn(ball.vy - min(self.depth, 1))

	kind = 'water'

	@property
	def pos(self):
		return Point(self.x, self.y)
