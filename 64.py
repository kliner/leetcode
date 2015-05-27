class Solution:
	# @param {integer[][]} grid
	# @return {integer}
	def minPathSum(self, grid):
		if len(grid) == 0 or len(grid[0]) == 0:
			return 0
		x = len(grid)
		y = len(grid[0])
		a = []
		for i in range(x):
			a.append([0 for j in range(y)])
		for i in range(x):
			for j in range(y):
				if i == 0 and j == 0:
					a[i][j] = grid[i][j]
				elif i == 0:
					a[i][j] = a[i][j-1] + grid[i][j]
				elif j == 0:
					a[i][j] = a[i-1][j] + grid[i][j]
				else:
					a[i][j] = min(a[i][j-1], a[i-1][j]) + grid[i][j]
		return a[x-1][y-1]

test = Solution()
print test.minPathSum([[1,2,3], [2,3,4], [3,4,5]])
print test.minPathSum([[1,1,1], [2,3,1], [3,4,5]])