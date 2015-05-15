class Solution:
	def judgeLine(self, a):
		# print a	
		d = {}
		for i in xrange(9):
			if a[i] == '.':
				continue
			if a[i] > '0' and a[i] <= '9':
				if a[i] in d:
					return False
				else:
					d[a[i]] = 1
			else:
				return False
		return True

	# @param {character[][]} board
	# @return {boolean}
	def isValidSudoku(self, board):
		for i in xrange(9):
			if not self.judgeLine(board[i][:]):
				return False
		for i in xrange(9):
			a = []
			for j in xrange(9):
				a.append(board[j][i])
			if not self.judgeLine(a):
				return False
		for i in xrange(3):
			for j in xrange(3):
				a = []
				a.extend(board[i*3][j*3:j*3+3])
				a.extend(board[i*3+1][j*3:j*3+3])
				a.extend(board[i*3+2][j*3:j*3+3])
				if not self.judgeLine(a):
					return False

		return True

test = Solution()
board = [
	['1','2','3','4','5','6','7','8','9'],
	['9','1','2','3','4','5','6','7','8'],
	['8','9','1','2','3','4','5','6','7'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.']
]
print test.isValidSudoku(board)
board = [
	['1','2','3','4','5','6','7','8','9'],
	['7','8','9','1','2','3','4','5','6'],
	['4','5','6','7','8','9','1','2','3'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.']
]
print test.isValidSudoku(board)