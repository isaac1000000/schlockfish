from game import gameboard
from game.pieces import *
curr_board = gameboard.BoardState(0, (39, 39))
curr_board.board = [
	[Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight (1), Rook(1)],
	[Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
	[Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)],
]

board1 = curr_board.move((7,1), [(5,2)])
board2 = board1.move((0,6), [(2,5)])
board3 = board2.move((5,2), [(4,4)])
board4 = board3.move((2,5), [(4,4)])
board5 = board4.move((6,3), [(5,3)])
board6 = board5.move((1,2), [(3,2)])

print(curr_board)
print("|\nv")
print(board1)
print("|\nv")
print(board2)
print("|\nv")
print(board3)
print("|\nv")
print(board4)
print("|\nv")
print(board5)
print("|\nv")
print(board6)

for move in King(1).get_moves((0,4)):
	print(move)