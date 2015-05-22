class Solution:
	ans = 0
	ls = []
	rs = []
	row = []
	# @param {integer} n
	# @return {integer}
	def totalNQueens(self, n):
		self.ans = 0
		self.ls = [0 for x in range(n*2)]
		self.rs = [0 for x in range(n*2)]
		self.row = [0 for x in range(n)]
		self.solve(n, 0)
		return self.ans

	def solve(self, n, cur):
		if cur == n:
			self.ans += 1
			return
		for i in range(n):
			if self.row[i] == self.ls[i+cur] == self.rs[cur+n-i] == 0:
				self.row[i] = self.ls[i+cur] = self.rs[cur+n-i] = 1
				self.solve(n, cur+1)
				self.row[i] = self.ls[i+cur] = self.rs[cur+n-i] = 0
		
test = Solution()
print test.totalNQueens(8)