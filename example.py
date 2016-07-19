import time

from Util import Point
from Ball import Ball
from Board import Board

from worlds import *
board = getVariedWorld()

print('\n'*100)
print(board)
for i in range(50):
    board.update()
    print ('\n'*100)
    print(board)
    time.sleep(0.1 )
