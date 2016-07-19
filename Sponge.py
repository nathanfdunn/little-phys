from Util import Point
from Locatable import Locatable

class SpongeElement(Locatable):
	def __init__(self, x, y, depth):
		super(self, Locatable).__init__(x, y)

	isYielding = False

	def bounceBall(self, ball):
		ball.vy += 1
