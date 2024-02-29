from board import Board
from cpu import playCpu
board = Board()

playing = True

while playing:
    
    board.takePlayerTurn()
    playCpu(board)
    
    if board.winner is not None:
        playing = False
