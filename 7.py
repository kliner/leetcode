class Solution:
	# @param x, an integer
	# @return an integer
	def reverse(self, x):
		maxint = 2147483647
		minint = -2147483648
		if x == 0:
			return 0
		if x < 0:
			x = -x
			f = True
		else:
			f = False
		a = []
		while x >= 10:
			a.append(x % 10)
			x = x / 10
		a.append(x)
		print a
		i = 0
		while a[i] == 0:
			i = i + 1
		b = 0
		while i < len(a):
			b = b * 10 + a[i]
			i = i + 1
		if (f and -b < minint) or (f == False and b > maxint):
			return 0
		else:
			if f:
				return -b
			else:
				return b

test = Solution()
print test.reverse(-2147483412)