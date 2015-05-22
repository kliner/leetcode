class Solution:
	# @param {integer[][]} matrix
	# @return {void} Do not return anything, modify matrix in-place instead.
	def rotate(self, matrix):
		n = len(matrix)
		for i in range(n):
			for j in range(i, n-1-i):
				t = matrix[i][j]
				matrix[i][j] = matrix[n-j-1][i]
				matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
				matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
				matrix[j][n-i-1] = t

test = Solution()
m = [[1,2,3],[4,5,6],[7,8,9]]
#123 741
#456 852
#789 963
test.rotate(m)
print m
