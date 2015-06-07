import copy
class Solution:
	ans = []
	# @param {integer} n
	# @return {integer[]}
	def grayCode(self, n):
		self.ans = []
		if n == 0:
			return [0]
		self.dfs("", n-1, True)
		return self.ans

	def dfs(self, pre, n, f):
		if n == 0:
			if f:
				self.ans.append(copy.copy(int(pre+str(0), 2)))
				self.ans.append(copy.copy(int(pre+str(1), 2)))
			else:
				self.ans.append(copy.copy(int(pre+str(1), 2)))
				self.ans.append(copy.copy(int(pre+str(0), 2)))
		else:
			if f:
				self.dfs(pre+str(0), n-1, True)
				self.dfs(pre+str(1), n-1, False)
			else:
				self.dfs(pre+str(1), n-1, True)
				self.dfs(pre+str(0), n-1, False)

test = Solution()
print test.grayCode(3)
print test.grayCode(4)
# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100