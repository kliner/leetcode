class Solution:
	# @param {integer} num
	# @return {string}
	def intToRoman(self, num):
		lst = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
		dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: '?', 10000: '?'}
		a = []
		while num >= 10:
			a.append(num % 10)
			num /= 10
		a.append(num)
		# print a
		res = ""
		for i in range(len(a)):
			one = lst[i*2]
			five = lst[i*2+1]
			ten = lst[i*2+2]
			if a[i] == 5:
				res = dic[five] + res
			elif a[i] > 5:
				if a[i] % 5 == 4:
					res = dic[one] + dic[ten] + res
				else:
					t = dic[five]
					for j in range(a[i] - 5):
						t = t + dic[one]
					res = t + res
			else:
				if a[i] % 5 == 4:
					res = dic[one] + dic[five] + res
				else:
					for j in range(a[i]):
						res = dic[one] + res
		return res

test = Solution()
print test.intToRoman(1), 'I'
print test.intToRoman(2), 'II'
print test.intToRoman(3), 'III'
print test.intToRoman(4), 'IV'
print test.intToRoman(5), 'V'
print test.intToRoman(6), 'VI'
print test.intToRoman(7), 'VII'
print test.intToRoman(8), 'VIII'
print test.intToRoman(9), 'IX'
print test.intToRoman(10), 'X'
print test.intToRoman(45), 'XLV'
print test.intToRoman(100), 'C'
print test.intToRoman(900), 'CM'
print test.intToRoman(990), 'CMXC'
print test.intToRoman(999), 'CMXCIX'
print test.intToRoman(1999), 'MCMXCIX'
print test.intToRoman(2008), 'MMVIII'
print test.intToRoman(2010), 'MMX'
print test.intToRoman(2018), 'MMXVIII'
print test.intToRoman(2019), 'MMXIX'

