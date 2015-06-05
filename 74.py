class Solution:
	# @param {integer[][]} matrix
	# @param {integer} target
	# @return {boolean}
	def searchMatrix(self, matrix, target):
		return self.searchCol(matrix, target)

	def searchCol(self, matrix, target):
		if len(matrix) == 1:
			return self.searchRow(matrix[0], target)
		else:
			n = len(matrix)
			if target < matrix[n >> 1][0]:
				return self.searchCol(matrix[:n >> 1], target)
			elif target > matrix[n >> 1][0]:
				return self.searchCol(matrix[n >> 1:], target)
			else:
				return True

	def searchRow(self, row, target):
		if len(row) == 0:
			return False
		elif len(row) == 1:
			return row[0] == target
		else:
			n = len(row)
			print row
			if target < row[n >> 1]:
				return self.searchRow(row[:n >> 1], target)
			elif target > row[n >> 1]:
				return self.searchRow(row[n >> 1:], target)
			else:
				return True

test = Solution()
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3)
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 10)
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 23)
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 30)
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 0)
print test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 51)