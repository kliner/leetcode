class Solution:
	# @param {integer} n
	# @return {integer}
	def climbStairs(self, n):
		if n <= 1:
			return 1
		a = [0 for i in range(n+1)]
		a[0] = 1
		a[1] = 1
		for i in range(2, n+1):
			a[i] = a[i-1] + a[i-2]
		return a[n]

test = Solution()
print test.climbStairs(1)
print test.climbStairs(2)
print test.climbStairs(3)