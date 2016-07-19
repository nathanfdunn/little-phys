from Util import Point, sgn
# Just a zero dampening deflector

class Deflector:
	# dir in '/\\'
	def __init__(self, dir, x, y):
		self.x = x
		self.y = y
		self.dir = dir

	isYielding = False

	@property
	def pos(self):
		return Point(self.x, self.y)
	
	def deflectBall(self, ball):
		# print('deflector before: ', ball)
		vx, vy = ball.vx, ball.vy
		if self.dir == '/':
			# if vx * vy #TODO make sure vel isn't parallel to dir
			ball.x += sgn(vy)
			ball.y += sgn(vx)
			ball.vx = vy
			ball.vy = vx
		elif self.dir == '\\':
			ball.x -= sgn(vy)
			ball.y -= sgn(vx)
			ball.vx = -vy
			ball.vy = -vx
		else:
			raise Exception('Unrecognized Deflector dir: '+self.dir)
		# print('deflector after: ', ball)

