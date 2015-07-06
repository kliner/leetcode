import copy
class Solution:
	# @param {string} s
	# @return {string[][]}
	def partition(self, s):
		l = len(s)
		if l == 0:
			return []
		self.ans = []
		self.path = []
		self.dfs(s, 0)
		return self.ans

	def isP(self, s):
		a = 0
		b = len(s) - 1
		while a <= b:
			if s[a] == s[b]:
				a += 1
				b -= 1
			else:
				return False
		if a > b:
			return True
		else:
			return False
		
	def dfs(self, s, start):
		if len(s) == start:
			self.ans.append(copy.copy(self.path))
			return
		for i in range(start + 1, len(s) + 1):
			if self.isP(s[start:i]):
				self.path.append(s[start:i])
				self.dfs(s, i)
				self.path.pop()

test = Solution()
print test.partition("")
print test.partition("aab")