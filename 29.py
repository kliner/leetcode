class Solution:
	# @param {integer} dividend
	# @param {integer} divisor
	# @return {integer}
	def divide(self, dividend, divisor):
		MIN_INT = -2147483648
		MAX_INT = 2147483647
		if divisor == 0:
			return MAX_INT

		f = False
		if dividend < 0 and divisor < 0:
			dividend = -dividend
			divisor = -divisor

		if divisor < 0:
			f = True
			divisor = -divisor

		if dividend < 0:
			f = True
			dividend = -dividend

		d = [divisor]
		a = [1]
		while divisor <= dividend:
			divisor = (divisor << 3) + (divisor << 1)
			a.append((a[len(d)-1] << 3) + (a[len(d)-1] << 1))
			d.append(divisor)

		n = len(a) - 2
		ans = 0
		for i in range(n, -1, -1):
			while dividend >= d[i]:
				# print d[i], dividend
				ans += a[i]
				dividend -= d[i]
		
		# if f and dividend > 0:
		# 	ans += 1

		if f:
			ans = -ans

		if ans > MAX_INT or ans < MIN_INT:
			return MAX_INT
		else:
			return ans


test = Solution()
print test.divide(1, 0)
print test.divide(1, 1)
print test.divide(10, 1)
print test.divide(1, 10)
print test.divide(1, -1)
print test.divide(10, -1)
print test.divide(1, -10)
print test.divide(123456789, 2345)
print test.divide(-123456789, 2345)
print test.divide(-2147483648, -1)
print test.divide(-2147483648, 0)