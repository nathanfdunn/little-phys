
from Water import WaterElement
from Barrier import Barrier
from Board import Board
from Deflector import Deflector
from Ball import Ball

from Util import DEFAULT_DIMENSION, Dimension

def generateBarrierBox(dim):
    out = [[None]*dim.width for i in range(dim.height)]

    for x in range(dim.width):
        for y in range(dim.height):
            if not(1 <= x < dim.width-1 and 1 <= y < dim.height -1):
                normals = ''
                # Needs vertical face
                if x in [0, dim.width-1]:
                    normals += '|'
                if y in [0, dim.height-1]:
                    normals += '-'
                out[y][x] = Barrier(x, y, normals)
    return out

def flatten2dArray(array):
    return [el for el in sum(array, []) if el is not None]

# Dim is the bounding box, so offset by 1
def generateWater(dim, depth):
    for x in range(1, dim.width-1):
        for y in range(1, min(depth+1, dim.height-1)):
            yield WaterElement(x, y, 4)

def generateDeflectors():
    for i in range(1, 5):
        yield Deflector('/', i+10, i)

def getBarrierWorld():
    barriers = flatten2dArray(generateBarrierBox(DEFAULT_DIMENSION))
    balls = [Ball(5, 1, 10, 5)]
    return Board(barriers=barriers, balls=balls)

def getBarrierWorld2():
    barriers = generateBarrierBox(DEFAULT_DIMENSION)
    barriers[1][10] = Barrier(10, 1, '|-')
    barriers[0][10] = Barrier(10, 0, '|-')
    barriers = flatten2dArray(barriers)
    balls = [Ball(5, 1, 10, 5)]
    return Board(barriers=barriers, balls=balls)

def getDeflectorWorld():
    barriers = flatten2dArray(generateBarrierBox(DEFAULT_DIMENSION))
    deflectors = generateDeflectors()
    balls = [Ball(13, 5, 0, 0)]
    
    return Board(barriers=list(barriers), deflectors=list(deflectors), balls=balls)

def getDeflectorWorld2():
    barriers = flatten2dArray(generateBarrierBox(DEFAULT_DIMENSION))
    barriers.append(Barrier(11,3,''))
    barriers.append(Barrier(12,3,''))
    deflectors = [
        Deflector('/',10, 4),
        Deflector('\\',13, 4)
    ]
    balls = [Ball(10, 0, 0, 10)]
    
    return Board(barriers=list(barriers), deflectors=list(deflectors), balls=balls)

def getWaterWorld():
    barriers = generateBarrierBox(DEFAULT_DIMENSION)
    water = generateWater(DEFAULT_DIMENSION, 4)
    balls = [Ball(2, 3, 0, 3)]
    return Board(barriers=list(barriers), water=list(water), balls=balls)


''' (Reference)
####################
#                  #
#      /           #
#                  #
#        #         #
#        #~~~~~~~~~#
#        #         #
#      O #         #
# \    / #         #
####################
'''

def getVariedWorld():
    dim = Dimension(20, 10)
    barriers = flatten2dArray(generateBarrierBox(dim))
    for i in range(1, 6):
        barriers.append(Barrier(9, i, '|'))
    deflectors = [
        Deflector('\\', 2, 1),
        Deflector('/', 7, 1),
        Deflector('/', 7, 7)
    ]
    balls = [Ball(2, 8, 0, 0)]

    water = []
    for x in range(10, 19):
        for y in range(1, 5):
            water.append(WaterElement(x,y,4))
    
    return Board(dim=dim, barriers=list(barriers), deflectors=list(deflectors), balls=balls, water=water)
