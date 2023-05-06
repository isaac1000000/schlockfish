import sys
sys.path.append("..")
from engine import schlockfish
from game import gameboard
from game.pieces import *

new_board = gameboard.BoardState(0, (39, 39))
new_board.board = [
	[Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight (1), Rook(1)],
	[Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
	[Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)]
]

sample_board = gameboard.BoardState(0, (24, 17))
sample_board.board = [
	[None, Knight(1), Bishop(1), None, None, Queen(0), None, None],
	[None, Pawn(1), None, None, None, None, None, None],
	[Rook(1), None, None, None, Pawn(1), None, None, None],
	[Pawn(1), None, None, None, Knight(1), None, King(1), None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, Pawn(0), None, None, None, None],
	[Pawn(0), King(0), Pawn(0), None, None, None, Pawn(0), Pawn(0)],
	[None, None, None, None, None, Rook(0), None, Rook(0)]
]

print(schlockfish.best_next_move(new_board))
print(schlockfish.best_next_move(sample_board))
