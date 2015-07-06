class Solution:
	# @param {string} s
	# @return {integer}
	def minCut(self, s):
		n = len(s)
		if n == 0:
			return 0
		a = []
		for i in range(n):
			a.append([0 for i in range(n)])
		dp = [n-i for i in range(n+1)]
		for i in range(n-1, -1, -1):
			for j in range(i, n):
				if s[i] == s[j] and (j-i<2 or a[i+1][j-1]):
					a[i][j] = True
					dp[i] = min(dp[i], dp[j+1]+1)
		return dp[0]-1
test = Solution()
print test.minCut("")
print test.minCut("a")
print test.minCut("ab")
print test.minCut("aab")