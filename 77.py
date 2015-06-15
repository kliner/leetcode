import copy
class Solution:
	ans = []
	# @param {integer} n
	# @param {integer} k
	# @return {integer[][]}
	def combine(self, n, k):
		self.ans = []
		self.dfs(n, k, [])
		return self.ans
		
	def dfs(self, n, k, cur):
		l = len(cur)
		if l == k:
			self.ans.append(copy.copy(cur))
			return
		if l == 0:
			start = 0
		else:
			start = cur[-1]
		for i in range(start, n):
			cur.append(i+1)
			self.dfs(n, k, cur)
			cur.pop()

test = Solution()
print test.combine(4,2)