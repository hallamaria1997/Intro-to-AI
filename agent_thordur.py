import numpy as np
import random

class Agent:
	def __init__(self, name=None, board=None):
		self.name = name
		self.boardAPI = board
		self.update_board()
		self.n_rows, self.n_cols = self.board.shape
		self.dirs = ['l', 'r', 'u', 'd']
		self.player = 1 # temporary solution: indicates this is the second player. Will later be able to distinguish between two agents
	
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
	
	def eval(self, board, maxRow):

		white_paths = self.find_paths(board, 1)
		black_paths = self.find_paths(board, 2)

		#print(white_paths[0])
		#print(black_paths[0])

		if(maxRow):
			return len(white_paths[0]) - len(black_paths[0])
		else:
			return len(black_paths[0]) - len(white_paths[0])
			

	def minimax(self, boardInstance, player, depth, maxRow):

		if(maxRow):
			currentParentScore = -81
		else:
			currentParentScore = 81

		currentParentMove = [[-1,-1], -1, -1]

		#print(depth)
		if(depth == 2):
			#print(boardInstance)
			#print(self.eval(boardInstance, maxRow))
			return self.eval(boardInstance, maxRow), currentParentMove

		available_moves = self.get_available_moves(boardInstance)

		#print(boardInstance)

		for av in range(len(available_moves)):
		#for av in range(3):

			move = available_moves[av]

			#print(move)

			pos = move[0]
			r = move[1]
			c = move[2]
		
			
			tmpBoardInstance = np.copy(boardInstance)
			tmpBoardInstance[pos] = 1
			tmpBoardInstance[(pos[0] + r, pos[1] + c)] = 2

			#print(tmpBoardInstance)
			#print(boardInstance)
			#print(pos, r, c)
			childScore, childMove = self.minimax(tmpBoardInstance, player, depth + 1, not maxRow)
			#print(childScore)
			#print(tmpBoardInstance)

			#print("Childscore: ", childScore)

			if(maxRow):
				#print(childScore, currentParentScore)
				if childScore > currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
					#print(currentParentMove)
			else:
				if childScore < currentParentScore:
					currentParentScore = childScore
					currentParentMove = move
			
		return currentParentScore, currentParentMove


	def make_move(self):
		# Makes a random move
		# Does not (yet) know the available positions.
		#print('\n{} making move'.format(self.name))
		self.update_board()

		# Find available moves and pick a random one
		#available_moves = self.get_available_moves(self.board)
		#print('available moves', len(available_moves))
		# self.update_available_moves()

		#move = available_moves[random.randint(0, len(available_moves)-1)]
		#print(move)
		#pos = move[0]
		#r = move[1]
		#c = move[2]

		#print("Eval from mini",
		
		miniScore, miniMove = self.minimax(self.board, self.player, 0, True)#)

		move = miniMove
		#print(move)
		#print(miniScore)

		pos = move[0]
		r = move[1]
		c = move[2]

		#print(move)
		
		#print('available moves: ', len(available_moves))
		#print('Place tile on {} r={}, c={}'.format(pos,r,c))

		
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
		print('Evaluation function: ', self.eval(self.board))

	def print_board(self):
		print(self.board)

class AgentAPI:
	# Encapsulation for the Agent class
	def __init__(self, name, board):
		self.agent = Agent(name=name, board=board)

	def make_move(self):
		return self.agent.make_move()