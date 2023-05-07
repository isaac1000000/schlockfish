from engine import schlockfish
from game.gameboard import BoardState
from game.pieces import *
from os import system

color_input_text = "Would you like to play as white or black? Select 'W' or 'B': "

player_color = input(color_input_text).lower()
while player_color != 'w' and player_color != 'b':
	player_color = input(color_input_text).lower()

player_color = 0 if player_color == 'w' else 1

print("-----BEGIN GAME-----")

curr_board = BoardState(0, (39, 39))
curr_board.board = [
	[Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight (1), Rook(1)],
	[Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None],
	[Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
	[Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)]
]
print(curr_board)

#TODO: Checks for pretty much everything to prevent user error
def get_move_from_user():
	piece_input_text = "Input a piece's starting square in form 'A4': "
	piece = input(piece_input_text).lower()
	# Turns user string into location of src for move
	piece = (8-int(piece[1]), ord(piece[0])-97)
	while curr_board.board[piece[0]][piece[1]] == None:
		piece = input(piece_input_text).lower()
		piece = (8-int(piece[1]), ord(piece[0])-97)

	piece_literal = curr_board.board[piece[0]][piece[1]]
	dest_input_text = "Input the square you'd like to move to in form 'A4': "
	dest = input(dest_input_text).lower()
	dest = (8-int(dest[1]), ord(dest[0])-97)

	if isinstance(piece_literal, Pawn):
		piece_moves = curr_board.get_pawn_moves_at(piece)
	else:
		piece_moves = piece_literal.get_moves(piece)

	# Returns list with arguments for valid BoardState.move()
	for i in piece_moves:
		for index,j in enumerate(i):
			if j == dest:
				return [piece, i[:index+1]]

#if player_color == 1:
#	cpu_move()

while True:
	move = get_move_from_user()
	curr_board = curr_board.move(move[0], move[1])
	print(curr_board)
	print("Thinking...\n")
	curr_board = schlockfish.best_next_move(curr_board)
	print(curr_board)

