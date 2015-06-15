class Solution:
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
		
	# @param {character[][]} board
	# @param {string} word
	# @return {boolean}
	def exist(self, board, word):
		x = len(board)
		if x == 0:
			return False
		y = len(board[0])
		if y == 0:
			return False
		m = []
		for i in range(x):
			m.append([0 for j in range(y)])
		for i in range(x):
			for j in range(y):
				if self.dfs(board, word, m, i, j):
					return True
		return False

	def dfs(self, board, word, m, x, y):
		if board[x][y] == word[0] and m[x][y] == 0:
			if len(word) == 1:
				return True
			# print m
			# print word
			m[x][y] = 1
			for i in range(4):
				if x + self.dx[i] >= 0 and x + self.dx[i] < len(board) and y + self.dy[i] >= 0 and y + self.dy[i] < len(board[0]):
					if self.dfs(board, word[1:], m, x + self.dx[i], y + self.dy[i]):
						return True
			m[x][y] = 0

test = Solution()
print test.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 'abccee')
print test.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 'abcced')
print test.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 'abcc')
print test.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 'see')
print test.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 'abcb')
print test.exist([['a']], 'a')