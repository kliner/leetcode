class Solution:
	# @param {string} a
	# @param {string} b
	# @return {string}
	def addBinary(self, a, b):
		if len(a) == 0:
			return b
		if len(b) == 0:
			return a
		if len(a) < len(b):
			a, b = b, a
		a = a[::-1]
		b = b[::-1]
		c = ''
		carry = False
		for i in range(len(b)):
			# print a[i], b[i], carry
			if a[i] == '1' and b[i] == '1' and carry:
				c += '1'
			elif (a[i] == '1' and b[i] == '1') or ((a[i] == '1' or b[i] == '1') and carry):
				c += '0'
				carry = True
			elif a[i] == '1' or b[i] == '1' or carry:
				c += '1'
				carry = False
			else:
				c += '0'
		for i in range(len(b), len(a)):
			if a[i] == '1' and carry:
				c += '0'
			elif a[i] == '1' or carry:
				carry = False
				c += '1'
			else:
				c += '0'
		if carry:
			c += '1'
		c = c[::-1]
		return c

test = Solution()
print test.addBinary('1', '1')
print test.addBinary('1', '11')
print test.addBinary('111', '11')
print test.addBinary("1010", "1011")