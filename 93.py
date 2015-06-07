import copy
class Solution:
	# @param {string} s
	# @return {string[]}
	def restoreIpAddresses(self, s):
		self.ans = set([])
		self.dfs(s, 0, '')
		return list(self.ans)

	def dfs(self, s, n, last):
		if n == 4:
			if len(s) == 0:
				self.ans.add(copy.copy(last[:-1]))
			return
		l = len(s)
		if l < 4 - n:
			return
		if l-1 <= 3 * (3-n):
			self.dfs(s[1:], n+1, last+s[:1]+'.')
		if l-2 <= 3 * (3-n) and int(s[:2]) >= 10:
			self.dfs(s[2:], n+1, last+s[:2]+'.')
		if l-3 <= 3 * (3-n) and int(s[:3]) <= 255 and int(s[:3]) >= 100:
			self.dfs(s[3:], n+1, last+s[:3]+'.')

test = Solution()
print test.restoreIpAddresses('255255255255')
print test.restoreIpAddresses('2552552550')
print test.restoreIpAddresses('25525511135')
print test.restoreIpAddresses('25525500')
print test.restoreIpAddresses('1234')