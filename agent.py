import numpy as np
import random
import random

class Agent:
	def __init__(self, name=None, board=None):
		self.name = name
		self.boardAPI = board
		self.update_board()
		self.n_rows, self.n_cols = self.board.shape
		self.dirs = ['l', 'r', 'u', 'd']
		self.player = None

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
	
	def position_ok(self, board, pos, r, c):
		# Check if the position is ok
		n_rows, n_cols = board.shape

		if pos[0] + r + 1 > n_rows:
			return False
		if pos[0] + r < 0:
			return False
		if pos[1] + c + 1 > n_cols:
			return False
		if pos[1] + c < 0:
			return False
		if (board[pos] != 0 or board[(pos[0]+r, pos[1]+c)] != 0):
			return False
		return True
	
	def get_available_moves(self, board):
		moves = []
		rows, cols = board.shape

		for i in range(rows):
			for j in range(cols):
				for d in self.dirs:
					pos = (i, j)
					r, c = self.get_r_c(d)
					if self.position_ok(board, pos, r, c):
						moves.append((pos, r, c))

		return moves
		
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

	def find_paths(self, board, n):
		# Locations of the value n on the board
		locs = np.where(board==n)
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
	
	def eval(self, board, maxRow, player):

		white_paths = self.find_paths(board, 1)
		black_paths = self.find_paths(board, 2)

		if(player == 1):
			if(maxRow):
				return len(white_paths[0]) - len(black_paths[0])
			else:
				return len(black_paths[0]) - len(white_paths[0])
		else:
			if(maxRow):
				return len(black_paths[0]) - len(white_paths[0])
			else:
				return len(white_paths[0]) - len(black_paths[0])
				

	def eval2(self, board, maxRow, player):
		# I might make an array that keeps a score of "how extensible" the 
		# paths are, and then use these scores as weights to multiply the
		# lengths of the paths.
		# OR
		# I'll find the "active paths" which is paths that can be expanded at
		# all and give them the value 1 and the "closed paths" the value 0
		#print("evaluating for player: ", player)
		white_paths = self.find_paths(board, 1)
		black_paths = self.find_paths(board, 2)

		if(player == 1):
			if(maxRow):
				if(len(white_paths) > 1 and len(black_paths) > 1):
					return len(white_paths[0]) + len(white_paths[1]) - len(black_paths[0]) - len(black_paths[1])
				return len(white_paths[0]) - len(black_paths[0])
			else:
				if(len(white_paths) > 1 and len(black_paths) > 1):
					return len(black_paths[0]) + len(black_paths[1]) - len(white_paths[0]) - len(white_paths[1])
				return len(black_paths[0]) - len(white_paths[0])
		else:
			if(maxRow):
				if(len(white_paths) > 1 and len(black_paths) > 1):
					return len(black_paths[0]) + len(black_paths[1]) - len(white_paths[0]) - len(white_paths[1])
				return len(black_paths[0]) - len(white_paths[0])
			else:
				if(len(white_paths) > 1 and len(black_paths) > 1):
					return len(white_paths[0]) + len(white_paths[1]) - len(black_paths[0]) - len(black_paths[1])
				return len(white_paths[0]) - len(black_paths[0])
	
	def find_neighbors(self, pos):
		positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1])
					, (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]

		neighbors = [p for p in positions if (p[0] > -1 and p[0] < 9 and p[1] > -1 and p[1] < 9)]
		return neighbors

	def extensibility(self, paths, board):
		ext = np.array([])
		for path in paths:
			neighbors = set()
			for pos in path:
				neighbors = neighbors.union(set(self.find_neighbors(pos)))
				neighbor_values = np.array([board[n] for n in list(neighbors)])
			ext = np.append(ext, (neighbor_values==0).astype(int).sum())

		return ext

	def eval3(self, board, maxRow, player):
		white_paths = self.find_paths(board, 1)
		black_paths = self.find_paths(board, 2)

		white_lengths = np.array([len(i) for i in white_paths])
		black_lengths = np.array([len(i) for i in black_paths])

		white_ext = self.extensibility(white_paths, board)
		black_ext = self.extensibility(black_paths, board)

		if(player == 1):
			if(maxRow):
				return np.dot(white_lengths, white_ext) - np.dot(black_lengths, black_ext)
			else:
				return np.dot(black_lengths, black_ext) - np.dot(white_lengths, white_ext)
		else:
			if(maxRow):
				return np.dot(black_lengths, black_ext) - np.dot(white_lengths, white_ext)
			else:
				return np.dot(white_lengths, white_ext) - np.dot(black_lengths, black_ext)

	def minimax(self, boardInstance, player, depth, maxRow):
		if(maxRow):
			currentParentScore = -np.inf
		else:
			currentParentScore = np.inf

		currentParentMove = [[-1,-1], -1, -1]

		if(depth == 2):
			return self.eval2(boardInstance, maxRow, player), currentParentMove

		available_moves = self.get_available_moves(boardInstance)

		for av in range(len(available_moves)):

			move = available_moves[av]

			pos = move[0]
			r = move[1]
			c = move[2]
		
			
			tmpBoardInstance = np.copy(boardInstance)
			tmpBoardInstance[pos] = 1
			tmpBoardInstance[(pos[0] + r, pos[1] + c)] = 2

			childScore, childMove = self.minimax(tmpBoardInstance, player, depth + 1, not maxRow)

			if(maxRow):
				if childScore > currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
			else:
				if childScore < currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
			
		return currentParentScore, currentParentMove

	# Minimax with alpha-beta pruning
	def minimax_alphabeta(self, boardInstance, player, depth, maxRow, alpha, beta):

		if(maxRow):
			currentParentScore = -np.inf
		else:
			currentParentScore = np.inf

		currentParentMove = [[-1,-1], -1, -1]

		if(depth == 2):
			return self.eval3(boardInstance, maxRow, player), currentParentMove

		available_moves = self.get_available_moves(boardInstance)

		for av in range(len(available_moves)):

			move = available_moves[av]

			pos = move[0]
			r = move[1]
			c = move[2]
		
			
			tmpBoardInstance = np.copy(boardInstance)
			tmpBoardInstance[pos] = 1
			tmpBoardInstance[(pos[0] + r, pos[1] + c)] = 2

			childScore, childMove = self.minimax_alphabeta(tmpBoardInstance, player, depth + 1, not maxRow, alpha, beta)

			if(maxRow):
				if childScore > currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
					alpha = max(alpha, currentParentScore)
				if beta <= alpha:
					break
			else:
				if childScore < currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
					beta = min(beta, currentParentScore)
				if beta <= alpha:
					break			
			
		return currentParentScore, currentParentMove

	def random_move(self):
		x = random.randint(2,6)
		y = random.randint(2,6)
		pos = (x,y)
		r = random.randint(-1,1)
		c = random.randint(-1,1)
		
		if r == 1 and c == 0:
			return (pos), 1
		elif r == 0 and c == 1:
			return (pos), 2
		elif r == -1 and c == 0:
			return (pos[0] + r, pos[1] + c), 3
		elif r == 0 and c == -1:
			return (pos[0] + r, pos[1] + c), 4
		else:
			return (pos), 1


	def make_move(self, player):
		self.player = player
		self.update_board()

		#if we want random
		# Find available moves and pick a random one
		#available_moves = self.get_available_moves(self.board)
		#move = available_moves[random.randint(0, len(available_moves)-1)]

		miniScore, miniMove = self.minimax_alphabeta(self.board, self.player, 0, True, -np.inf, np.inf)

		move = miniMove

		pos = move[0]
		r = move[1]
		c = move[2]
		
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
		one_paths = self.find_paths(self.board, 1)
		two_paths = self.find_paths(self.board, 2)
		empty_paths = self.find_paths(self.board, 0)
		
		print('Longest sequence of whites: ', len(one_paths[0]))
		print('Longest sequence of blues: ', len(two_paths[0]))
		print('Longest path of empty', len(empty_paths[0]))

	def print_board(self):
		print(self.board)

class AgentAPI:
	# Encapsulation for the Agent class
	def __init__(self, name, board):
		self.agent = Agent(name=name, board=board)

	def make_move(self, player):
		return self.agent.make_move(player)

	def random_move(self):
		return self.agent.random_move()