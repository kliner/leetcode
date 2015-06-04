class Solution:
	# @param {integer[][]} matrix
	# @return {void} Do not return anything, modify matrix in-place instead.
	def setZeroes(self, matrix):
		x = len(matrix)
		if x == 0:
			return
		y = len(matrix[0])
		if y == 0:
			return
		x0 = 1
		y0 = 1
		for i in range(x):
			if matrix[i][0] == 0:
				x0 = 0
		for j in range(y):
			if matrix[0][j] == 0:
				y0 = 0
		for i in range(1, x):
			for j in range(1, y):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0
		for i in range(1, x):
			if matrix[i][0] == 0:
				for j in range(1, y):
					matrix[i][j] = 0
		for j in range(1, y):
			if matrix[0][j] == 0:
				for i in range(1, x):
					matrix[i][j] = 0
		if x0 == 0:		
			for i in range(x):
				matrix[i][0] = 0
		if y0 == 0:
			for j in range(y):
				matrix[0][j] = 0
		
test = Solution()
a = [[1,2,3],[2,3,4],[3,0,5]]
test.setZeroes(a)
print a
a = [[0,2,3],[2,3,4],[3,1,5]]
test.setZeroes(a)
print a
a = [[0,0,3],[2,3,4],[3,1,5]]
test.setZeroes(a)
print a