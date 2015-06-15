class Solution:
	# @param {integer} n
	# @return {integer}
	def numTrees(self, n):
		a = [0 for i in range(n+1)]
		a[0] = 1
		a[1] = 1
		if n < 2:
			return a[n]
		for i in range(2,n+1):
			for j in range(i):
				a[i] += a[j] * a[i-1-j]
		return a[n]

test = Solution()
print test.numTrees(1)
print test.numTrees(2)
print test.numTrees(3)
print test.numTrees(4)
