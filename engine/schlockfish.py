import sys
sys.path.append("..")

from game.gameboard import BoardState
from game.pieces import *

MAX_DEPTH = 3

# Very simple driver for clarity elsewhere
def best_next_move(board_state: BoardState) -> BoardState:
	return best_move(board_state, 0)

# DFS algorithm tries all possible moves and reports the best found at depth MAX_DEPTH
def best_move(board_state: BoardState, depth) -> BoardState:
	if board_state == None:
		return

	#Arbitrarily high scores for later comparison
	if board_state.next_turn == 0:
		best_score = -10000
	else:
		best_score = 10000

	# Difference of white score - black score
	next_best_move = None
	# Goes through each piece on the board
	for i in range(8):
		for j in range(8):
			# Current piece
			piece = board_state.board[i][j]
			# Finds a piece of color to move
			if piece != None and piece.color == board_state.next_turn:
				# Gets moveset generator
				if isinstance(piece, Pawn):
					move_gen = board_state.get_pawn_moves_at((i, j))
				else:
					move_gen = piece.get_moves((i, j))
				# move is a move path
				for move in move_gen:
					# move_index is the destination on that path
					# All valid moves are generated
					for move_index in range(len(move)):
						move_board_state = board_state.move((i,j), move[:move_index+1])

						if depth < MAX_DEPTH:
							best_of_move = best_move(move_board_state, depth+1)
						else:
							# Chooses best move by current state instead of analysis
							best_of_move = move_board_state

						if best_of_move == None:
							continue

						# Finds best score
						scores = best_of_move.scores
						if board_state.next_turn == 0:
							if scores[0] - scores[1] > best_score:
								next_best_move = move_board_state
								best_score = scores[0] - scores[1]
						else:
							if scores[0] - scores[1] < best_score:
								next_best_move = move_board_state
								best_score = scores[0] - scores[1]

	return next_best_move
