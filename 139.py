class Solution:
	# @param s, a string
	# @param wordDict, a set<string>
	# @return a boolean
	def wordBreak(self, s, wordDict):
		n = len(s)
		a = []
		for i in range(n+1):
			a.append([0 for j in range(n+1)])
		for i in range(n):
			for j in range(i+1, n+1):
				if s[i:j] in wordDict:
					a[i][j] = 1
		dp = [0 for i in range(n+1)]
		dp[0] = 1
		for i in range(n):
			if dp[i] == 1:
				for j in range(i, n+1):
					if a[i][j] == 1:
						dp[j] = 1
		# print dp
		return dp[n] == 1

test = Solution()
print test.wordBreak("", ["leet","code"])
print test.wordBreak("leetcode", ["leet","code"])
print test.wordBreak("leetcode", ["leet","cxxe"])
print test.wordBreak("leetcode", [])
print test.wordBreak("bb", ['a','b','bbb'])