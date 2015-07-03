class Solution:
	# @param {character[][]} board
	# @return {void} Do not return anything, modify board in-place instead.
	def solve(self, board):
		dx = [0, 1, 0, -1]
		dy = [1, 0, -1, 0]
		if len(board) <= 1:
			return
		if len(board[0]) <= 1:
			return
		m = len(board)
		n = len(board[0])
		cur = []
		for i in range(m):
			if board[i][0] == 'O':
				cur.append((i, 0))
			if board[i][-1] == 'O':
				cur.append((i, n-1))
		for i in range(n):
			if board[0][i] == 'O':
				cur.append((0, i))
			if board[-1][i] == 'O':
				cur.append((m-1, i))
		while len(cur):
			new = set([])
			for x, y in cur:
				board[x][y] = 'A'
				for i in range(4):
					if x+dx[i] >= 0 and x+dx[i] < m and y+dy[i] >= 0 and y+dy[i] < n and board[x+dx[i]][y+dy[i]] == 'O':
						new.add((x+dx[i], y+dy[i]))
			cur = new

		for i in range(m):
			for j in range(n):
				if board[i][j] == 'O':
					board[i][j] = 'X'
		for i in range(m):
			for j in range(n):
				if board[i][j] == 'A':
					board[i][j] = 'O'
		
test = Solution()
board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
test.solve(board)
print board
