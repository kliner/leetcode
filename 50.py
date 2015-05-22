class Solution:
	# @param {float} x
	# @param {integer} n
	# @return {float}
	def myPow(self, x, n):
		i = 1
		a = [(x,1)]
		f = False
		if n < 0:
			f = True
			n = -n
		t = n >> 1
		while i <= t:
			i = i << 1
			a.append((a[-1][0] ** 2, i))
		# print a
		ans = 1.0
		for p, i in a[::-1]:
			if n >= i:
				ans *= p
				n -= i
		if f:
			return 1.0/ans
		else:
			return ans

test = Solution()
print test.myPow(2, 10)
print test.myPow(2, 8)
print test.myPow(34, -3)