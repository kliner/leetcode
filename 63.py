class Solution:
	# @param {integer[][]} obstacleGrid
	# @return {integer}
	def uniquePathsWithObstacles(self, x):
		if len(x) == 0 or len(x[0]) == 0 or x[0][0] == 1:
			return 0
		n = len(x)
		m = len(x[0])
		if x[n-1][m-1] == 1:
			return 0
		a = []
		for i in range(n):
			a.append([0 for j in range(m)])
		for i in range(n):
			for j in range(m):
				# print i,j,a
				if i == 0 and j == 0:
					a[i][j] = 1
				elif x[i][j] == 1:
					a[i][j] = 0
				elif j == 0:
					a[i][j] = a[i-1][j]
				elif i == 0:
					a[i][j] = a[i][j-1]
				else:
					a[i][j] = a[i-1][j] + a[i][j-1]
		# print a
		return a[n-1][m-1]

test = Solution()
print test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0],[0,0,0]])