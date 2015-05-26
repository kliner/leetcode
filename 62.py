class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePaths(self, m, n):
		if m == 0 or n == 0:
			return 0
		a = []
		a.append([1 for j in range(n)])
		for i in range(1, m):
			a.append([0 for j in range(n)])
		
		for i in range(1, m):
			a[i][0] = a[i-1][0]
			for j in range(1, n):
				a[i][j] = a[i-1][j] + a[i][j-1]

		return a[m-1][n-1]

test = Solution()
print test.uniquePaths(0,0)
print test.uniquePaths(1,0)
print test.uniquePaths(0,1)
print test.uniquePaths(1,1)
print test.uniquePaths(3,7)

