class Solution:
	ans = []
	ls = []
	rs = []
	row = []
	# @return a list of lists of string
	def solveNQueens(self, n):
		self.ans = []
		m = []
		self.ls = [0 for x in range(n*2)]
		self.rs = [0 for x in range(n*2)]
		self.row = [0 for x in range(n)]
		for i in range(n):
			m.append(['.' for x in range(n)])
		self.solve(m, 0)
		return self.ans
		
	def solve(self, m, cur):
		n = len(m)
		if cur == n:
			a = []
			for a1 in m:
				s = ''
				for a2 in a1:
					s += a2
				a.append(s)
			self.ans.append(a)
			return
		for i in range(n):
			# print i, i+cur, cur+n-i
			if self.row[i] == self.ls[i+cur] == self.rs[cur+n-i] == 0:
				self.row[i] = self.ls[i+cur] = self.rs[cur+n-i] = 1 
				m[cur][i] = 'Q'
				self.solve(m, cur+1)
				m[cur][i] = '.'
				self.row[i] = self.ls[i+cur] = self.rs[cur+n-i] = 0

test = Solution()
print test.solveNQueens(4)
print len(test.solveNQueens(8))
