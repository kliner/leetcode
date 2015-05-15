class Solution:
	# @param {character[][]} board
	# @return {boolean}
	def isValidSudoku(self, board, x, y):
		for i in xrange(9):
			if i != x and board[i][y] == board[x][y]:
				return False
		for i in xrange(9):
			if i != y and board[x][i] == board[x][y]:
				return False
		for i in xrange(x / 3 * 3, x / 3 * 3 + 3):
			for j in xrange(y / 3 * 3, y / 3 * 3 + 3):
				if i != x and y != x and board[i][j] == board[x][y]:
					return False
		return True

	def solve(self, board):
		# print board
		for i in xrange(9):
			for j in xrange(9):
				# print i, j
				if board[i][j] == '.':
					for k in xrange(1,10):
						board[i][j] = chr(48+k)
						if self.isValidSudoku(board, i, j):
							if self.solve(board):
								return True
					board[i][j] = '.'
					return False
		return True

	# @param {character[][]} board
	# @return {void} Do not return anything, modify board in-place instead.
	def solveSudoku(self, board):
		self.solve(board)

test = Solution()
board = [
	['5','3','.','.','7','.','.','.','.'],
	['6','.','.','1','9','5','.','.','.'],
	['.','9','8','.','.','.','.','6','.'],
	['8','.','.','.','6','.','.','.','3'],
	['4','.','.','8','.','3','.','.','1'],
	['7','.','.','.','2','.','.','.','6'],
	['.','6','.','.','.','.','2','8','.'],
	['.','.','.','4','1','9','.','.','5'],
	['.','.','.','.','8','.','.','7','9']
]
test.solveSudoku(board)
print board