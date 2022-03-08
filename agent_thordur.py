import numpy as np
import random

class Agent:
	def __init__(self, name=None, board=None):
		self.name = name
		self.boardAPI = board
		self.update_board()
		self.n_rows, self.n_cols = self.board.shape
		self.dirs = ['l', 'r', 'u', 'd']
		self.available_moves = []
		self.one_paths = []
		self.zero_paths = []
	
	def update_board(self):
		self.board = self.boardAPI.get_board()

	def get_r_c(self, dir):
		# Translate the direction into numbers
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
		return r, c
	
	def position_ok(self, pos, r, c):
		# Check if the position is ok
		self.update_board()

		if pos[0] + r + 1 > self.n_rows:
			return False
		if pos[0] + r < 0:
			return False
		if pos[1] + c + 1 > self.n_cols:
			return False
		if pos[1] + c < 0:
			return False
		if self.board[pos] != 0 or self.board[pos[0]+r, pos[1]+c] != 0:
			return False
		return True
	
	def update_available_moves(self):
		self.board = self.boardAPI.get_board()
		moves = []

		for i in range(self.n_rows):
			for j in range(self.n_cols):
				for d in self.dirs:
					pos = (i, j)
					r, c = self.get_r_c(d)
					if self.position_ok(pos, r, c):
						moves.append((pos, r, c))

		self.available_moves = moves
		
	def is_adj(self, c1, c2):
		# Adjacent is only the cell directly above or by the side,
		# not diagonal
		s = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
		return s == 1

	def merge_paths(self, adj_lists):
		# Merge the neighbour lists into complete paths
		merges = 1
		while merges != 0:
			merges = 0
			for i, a in enumerate(adj_lists):
				for j, b in enumerate(adj_lists):
					if j != i and len(set(adj_lists[i]).intersection(set(b))) > 0:
						merges += 1
						new_set = list(set(adj_lists[i]).union(b))
						adj_lists[i] = new_set
						adj_lists[j] = []

		# Sort by length and delete empty paths
		adj_lists = sorted(adj_lists, key=lambda l: len(l), reverse=True)
		adj_lists = [i for i in adj_lists if len(i) > 0]
		return adj_lists

	def find_paths(self, n):
		# Locations of the value n on the board
		self.update_board()
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
		paths = self.merge_paths(adj_lists)

		return paths
	
	def eval(self):
		white_paths = self.find_paths(1)
		black_paths = self.find_paths(2)
		return len(white_paths[0]) - len(black_paths[0])

	def make_move(self):
		# Makes a random move
		# Does not (yet) know the available positions.
		print('\n{} making move'.format(self.name))
		self.update_board()
		self.print_paths()
		self.print_board()

		# Find available moves and pick a random one
		self.update_available_moves()
		move = self.available_moves[random.randint(0, len(self.available_moves)-1)]
		pos = move[0]
		r = move[1]
		c = move[2]
		
		print('available moves: ', len(self.available_moves))
		print('Place tile on {} r={}, c={}'.format(pos,r,c))
		
		if r == 1 and c == 0:
			return (pos), 1
		elif r == 0 and c == 1:
			return (pos), 2
		elif r == -1 and c == 0:
			return (pos[0] + r, pos[1] + c), 3
		elif r == 0 and c == -1:
			return (pos[0] + r, pos[1] + c), 4

	def print_paths(self):
		self.update_board()
		one_paths = self.find_paths(1)
		two_paths = self.find_paths(2)
		
		print('Longest sequence of whites: ', len(one_paths[0]))
		print('Longest sequence of blues: ', len(two_paths[0]))
		print('Evaluation function: ', self.eval())

	def print_board(self):
		print(self.board)

class AgentAPI:
	# Encapsulation for the Agent class
	def __init__(self, name, board):
		self.agent = Agent(name=name, board=board)

	def make_move(self):
		return self.agent.make_move()