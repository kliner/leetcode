class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		n = len(triangle)
		if n == 0:
			return 0
		a = []
		for i in range(n):
			a.append([0 for j in range(i+1)])

		a[0][0] = triangle[0][0]
		for i in range(1, n):
			for j in range(i+1):
				if j == 0:
					a[i][0] = a[i-1][0] + triangle[i][0]
				elif j == i:
					a[i][i] = a[i-1][i-1] + triangle[i][i]
				else:
					a[i][j] = min(a[i-1][j], a[i-1][j-1]) + triangle[i][j]
		return min(a[n-1])

test = Solution()
f = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print test.minimumTotal(f)