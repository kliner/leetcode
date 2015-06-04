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
		mx = [0 for i in range(x)]
		my = [0 for i in range(y)]
		for i in range(x):
			for j in range(y):
				if matrix[i][j] == 0:
					mx[i] = 1
					my[j] = 1
		for i in range(x):
			if mx[i] == 1:
				for j in range(y):
					matrix[i][j] = 0
		for i in range(y):
			if my[i] == 1:
				for j in range(x):
					matrix[j][i] = 0

test = Solution()
a = [[1,2,3],[2,3,4],[3,0,5]]
test.setZeroes(a)
print a