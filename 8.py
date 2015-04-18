class Solution:
	# @param str, a string
	# @return an integer
	def myAtoi(self, str):
		INT_MAX = 2147483647
		INT_MIN  = -2147483648
		state = 0
		posi = 1
		res = 0
		for i in range(len(str)):
			if state == 0 and str[i] == ' ':
				continue
			if state == 0 and str[i] == '-':
				posi = -1
				state = 1
				continue
			if state == 0 and str[i] == '+':
				posi = 1
				state = 1
				continue

			if state == 0:
				state = 1
			
			if state == 1 and str[i] == '0':
				continue

			if state == 1:
				state = 2

			if state == 2:
				try:
					t = int(str[i]) - 0
				except Exception, e:
					break

				if t >= 0 and t <= 9:
					res = res * 10 + t
				else:
					return 0
		res = res * posi
		if res > INT_MAX:
			return INT_MAX
		if res < INT_MIN:
			return INT_MIN
		return res

test = Solution()
print test.myAtoi('')
print test.myAtoi('test')
print test.myAtoi('-abc')
print test.myAtoi('--123')
print test.myAtoi('+23')
print test.myAtoi('++23')
print test.myAtoi('-123abc')
print test.myAtoi('-0123')
print test.myAtoi('-999999999999')
print test.myAtoi('99999999999')
print test.myAtoi('123')
print test.myAtoi('-123')