from board import Board
from random import randint

def playCpu(board):
    positions = board.getValidPositions()
    
    cpuOption = randint(0, len(positions)-1)
    
    board.playMove(cpuOption, "X")