import copy
class Solution:
	# @param s, a string
	# @param wordDict, a set<string>
	# @return a string[]
	def wordBreak(self, s, wordDict):
		n = len(s)
		a = []
		for i in range(n+1):
			a.append([0 for i in range(n+1)])
		dp = [0 for i in range(n+1)]
		dp[0] = 1
		for i in range(n):
			for j in range(i+1, n+1):
				if dp[i] and s[i:j] in wordDict:
					dp[j] = 1
					a[i][j] = 1

		self.ans = []
		if not dp[n]:
			return self.ans
		self.dfs(a, 0, n, [])
		r = []
		for ss in self.ans:
			last = 0
			t = ""
			for i in ss:
				t += s[last:i] + " "
				last = i
			r.append(t[:-1])
		return r

		
	def dfs(self, a, cur, n, route):
		if cur == n:
			self.ans.append(copy.copy(route))
			return
		for i in range(cur+1, n+1):
			if a[cur][i] == 1:
				route.append(i)
				self.dfs(a, i, n, route)
				route.pop()

test = Solution()
print test.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print test.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])