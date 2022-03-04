import numpy as np
import random
from board_thordur import BoardAPI

class Agent:
	def __init__(self):
		self.boardAPI = BoardAPI()
		self.board = self.get_board()
		self.n_rows, self.n_cols = self.board.shape
		self.dirs = ['l', 'r', 'u', 'd']
		self.available_moves = []	# Maybe useful later
	
	def get_board(self):
		return self.boardAPI.get_board()

	def position_ok(self, pos, r, c):
		self.board = self.get_board()

		if pos[0] + r + 1 > self.n_rows:
			return False
		if pos[0] + r < 0:
			return False
		if pos[1] + c + 1 > self.n_cols:
			return False
		if pos[1] + c < 0:
			return False
		if not np.isnan(self.board[pos]) or not np.isnan(self.board[pos[0]+r, pos[1]+c]):
			return False
		return True
		
	def is_adj(self, c1, c2):
		# Adjacent is only the cell directly above or by the side,
		# not diagonal
		s = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
		return s == 1

	def find_paths(self, n):
		# Locations of the value n on the board
		self.board = self.get_board()
		locs = np.where(self.board==n)
		coords = list(zip(locs[0], locs[1]))
		adj_lists = []

		# Finds the neighbour of each n-value
		for i, c1 in enumerate(coords):
			adj_lists.append([c1])
			for j, c2 in enumerate(coords):
				if i != j and self.is_adj(c1, c2):
					adj_lists[i].append(c2)
		
		# Merges the neighbors into paths
		merges = 1
		while merges != 0:
			merges = 0
			for i, a in enumerate(adj_lists):
				for j, b in enumerate(adj_lists):
					if j > i and len(set(a).intersection(set(b))) > 0:
						merges += 1
						new_set = list(set(a).union(b))
						adj_lists[i] = new_set
						adj_lists[j] = []

		# Sort by length and delete empty paths
		adj_lists = sorted(adj_lists, key=lambda l: len(l), reverse=True)
		adj_lists = [i for i in adj_lists if len(i) > 0]
		return adj_lists

	def make_move(self):
		# Makes a random move
		# Does not (yet) know the available positions.
		self.board = self.get_board()
		row = random.randint(0, self.n_rows-1)
		col = random.randint(0, self.n_cols-1)
		dir = self.dirs[random.randint(0,3)]
		pos = tuple([row, col])
		r = 0
		c = 0

		if dir == 'r':
			r = 0
			c = 1
		elif dir == 'l':
			r = 0
			c = -1
		elif dir == 'u':
			r = -1
			c = 0
		elif dir == 'd':
			r = 1
			c = 0
		
		if not self.position_ok(pos, r, c):
			self.make_move()
		else:
			print('Place tile on {}, direction {}'.format(pos, dir))
			self.boardAPI.place_tile(pos, r, c)
		
		self.print_board()
		self.print_paths()

	def print_paths(self):
		zero_paths = self.find_paths(0)
		one_paths = self.find_paths(1)
		
		print('Zeros paths', len(zero_paths))
		print('Longest sequence of zeros: ', len(zero_paths[0]))
		print('One paths', len(one_paths))
		print('Longest sequence of ones: ', len(one_paths[0]))

	def print_board(self):
		print(self.board)

class AgentAPI:
	# Encapsulation for the Agent class
	def __init__(self):
		self.agent = Agent()

	def make_move(self, ):
		self.agent.make_move()