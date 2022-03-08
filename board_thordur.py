import numpy as np

class Board:
	# A mock-class representing the game board.
	# We will then replace this by the game-class or whatever 
	# is used for the board.
	def __init__(self):
		self.n_rows = 9
		self.n_cols = 9
		self.board = np.empty([self.n_rows, self.n_cols])
		self.one_paths = []
		self.zero_paths = []
		# We will probably change this to 0 .....
		self.board[:,:] = np.NaN
	
	def get_board(self):
		return self.board

	def place_tile(self, pos, r, c):
		# .....and change this to 1 and -1
		self.board[pos] = 0
		self.board[pos[0] + r, pos[1] + c] = 1

class BoardAPI:
	# An encapsulation for the Board class
	def __init__(self):
		self.board = Board()
	
	def get_board(self):
		board = self.board.get_board()
		return board

	def place_tile(self, pos, r, c):
		self.board.place_tile(pos, r, c)