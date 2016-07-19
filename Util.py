from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

Dimension = namedtuple('Dimension', ['width', 'height'])

DEFAULT_DIMENSION = Dimension(20, 8)

def sgn(x):
    if x < 0: return -1
    if x > 0: return 1
    return 0
