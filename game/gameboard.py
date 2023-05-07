from .pieces import *

"""
Contains one single possible arrangement of the pieces, used to generate
potential moves from the actual state of the board
"""
#TODO: Check and checkmate flags/signals
class BoardState:

	def __init__(self, next_turn, scores: tuple):
		# 0 for white, 1 for black
		self.next_turn = next_turn
		# tuple with white's score index as 0
		self.scores = scores
		# Stores pieces currently on the game board
		self.board = [
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None]
		]

	def __str__(self):
		result_string = "\u0332".join("  A B C D E F G H  ") + "\n"
		for i in range(8):
			result_string += str(8-i) +  "|"
			for j in range(8):
				if self.board[i][j] == None:
					result_string += " |"
				else:
				 result_string += str(self.board[i][j]) + "|"
			result_string += "\n"
		return result_string

	# Dest is a list of tuples from the first step in the move to the destination
	# Returns None if there is a piece in the way
	def move(self, src: tuple, dest: list):
		# Check for valid move
		piece_to_move = self.board[src[0]][src[1]]
		for step in dest[:-1]:
			if self.board[step[0]][step[1]] != None:
				return None

		# Copy current board array into new board array
		new_board = [
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None]
		]
		for i in range(8):
			for j in range(8):
				new_board[i][j] = self.board[i][j]

		# Adjust score if capturing
		piece_on_dest = self.board[dest[-1][0]][dest[-1][1]]
		if piece_on_dest != None:
			if piece_to_move.color != piece_on_dest.color:
				if piece_on_dest.color == 1:
					new_scores = (self.scores[0], self.scores[1]-piece_on_dest.pawns)
				else:
					new_scores = (self.scores[0]-piece_on_dest.pawns, self.scores[1])

			else:
				return None
		else:
			new_scores = self.scores

		# Replace dest with piece on src
		new_board[dest[-1][0]][dest[-1][1]] = new_board[src[0]][src[1]]
		new_board[src[0]][src[1]] = None

		# Create new board state and return
		result_board_state = BoardState(not self.next_turn, new_scores)
		result_board_state.board = new_board
		return result_board_state


	# Generates moves for a pawn considering diagonal captures and two-steps
	def get_pawn_moves_at(self, src:tuple):
		pawn = self.board[src[0]][src[1]]
		# Black pawns
		if pawn.color == 1:
			# Two-square move
			if src[0] == 1:
				if self.board[src[0]+2][src[1]] is None:
					yield [(src[0]+1, src[1]), (src[0]+2, src[1])]
			else:
				if self.board[src[0]+1][src[1]] is None:
					yield [(src[0]+1, src[1])]
			# Diagonal captures
			if src[1] > 0 and self.board[src[0]+1][src[1]-1] is not None:
				yield [(src[0]+1, src[1]-1)]
			if src[1] < 7 and self.board[src[0]+1][src[1]+1] is not None:
				yield [(src[0]+1, src[1]+1)]
		# White pawns
		else:
			# Two-square move
			if src[0] == 6:
				if self.board[src[0]-2][src[1]] is None:
					yield [(src[0]-1, src[1]), (src[0]-2, src[1])]
			else:
				if self.board[src[0]-1][src[1]] is None:
					yield [(src[0]-1, src[1])]
			# Diagonal captures
			if src[1] > 0 and self.board[src[0]-1][src[1]-1] is not None:
				yield [(src[0]-1, src[1]-1)]
			if src[1] < 7 and self.board[src[0]-1][src[1]+1] is not None:
				yield [(src[0]-1, src[1]+1)]

