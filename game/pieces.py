"""
Abstract class for a single piece
"""
class Piece:
	def __init__(self, color, pawns):
		self.color = color
		self.pawns = pawns

	# Generator that supplies all valid moves for the position of the piece
	# One list for each direction, in the order that that piece would move 
	# one square at a time
	@staticmethod
	def get_moves(position):
		pass

		

class Queen(Piece):
	def __init__(self, color):
		super().__init__(color, 9)

	@staticmethod
	def get_moves(position):
		for i in Rook.get_moves(position):
			yield i
		for i in Bishop.get_moves(position):
			yield i

	def __str__(self):
		return "♛" if self.color == 0 else "♕"



class Bishop(Piece):
	def __init__(self, color):
		super().__init__(color, 3)

	@staticmethod
	def get_moves(position):
		x = position[0]
		y = position[1]
		yield [(x+i, y+i) for i in range(1, 8) if x+i<8 and y+i<8]
		yield [(x-i, y-i) for i in range(1, 8) if x-i>=0 and y-i>=0]
		yield [(x+i, y-i) for i in range(1, 8) if x+i<8 and y-i>=0]
		yield [(x-i, y+i) for i in range(1, 8) if x-i>=0 and y+i<8]

	def __str__(self):
		return "♝" if self.color == 0 else "♗"




class Rook(Piece):
	def __init__(self, color):
		super().__init__(color, 5)

	@staticmethod
	def get_moves(position):
		yield [(i, position[1]) for i in range(position[0]-1, -1, -1)]
		yield [(i, position[1]) for i in range(position[0]+1, 8)]
		yield [(position[0], i) for i in range(position[1]-1, -1, -1)]
		yield [(position[0], i) for i in range(position[1]+1, 8)]

	def __str__(self):
		return "♜" if self.color == 0 else "♖"


class Knight(Piece):
	def __init__(self, color):
		super().__init__(color, 3)

	@staticmethod
	def get_moves(position):
		# Possible patterns for knight moves
		for x, y in [(1, 2), (-1, 2), (1, -2), (-1, -2)]:
			if 0 <= position[0] + x < 8 and 0 <= position[1] + y < 8:
				yield [(position[0] + x, position[1] + y)]
			if 0 <= position[0] + y < 8 and 0 <= position[1] + x < 8:
				yield [(position[0] + y, position[1] + x)]

	def __str__(self):
		return "♞" if self.color == 0 else "♘"


class Pawn(Piece):
	def __init__(self, color):
		super().__init__(color, 1)

	# Pawn moves are handled by the gameboard object because it relies on
	# being able to see the pieces around the pawn and the pawns color.
	# But Pawn still needs a get_moves method to not cause errors
	@staticmethod
	def get_moves(position):
		pass

	def __str__(self):
		return "♟" if self.color == 0 else "♙"

class King(Piece):
	def __init__(self, color):
		# King is given an arbitrarily high pawn value to simplify engine
		super().__init__(color, 1000)

	@staticmethod
	def get_moves(position):
		if position[0] < 7:
			yield [(position[0]+1, position[1])]
			if position[1] < 7:
				yield [(position[0]+1, position[1]+1)]
			if position[1] > 0:
				yield [(position[0]+1, position[1]-1)]
		if position[0] > 0:
			yield [(position[0]-1, position[1])]
			if position[1] > 0:
				yield [(position[0]-1, position[1]-1)]
			if position[1] < 7:
				yield [(position[0]-1, position[1]+1)]
		if position[1] < 7:
			yield [(position[0], position[1]+1)]
		if position[1] > 0:
			yield [(position[0], position[1]-1)]



	def __str__(self):
		return "♚" if self.color == 0 else "♔"
