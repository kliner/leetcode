class Solution:
	# @param {string} s
	# @return {integer}
	def romanToInt(self, s):
		lst = [1, 5, 10, 50, 100, 500, 1000]
		dic = {'I': (1, 1), 'V': (2, 5), 'X': (2, 10), 'L': (3, 50), 'C': (3, 100), 'D': (4, 500), 'M': (4, 1000)}
		i = 0
		n = len(s)
		res = 0
		while i < n - 1:
			if dic[s[i+1]][0] == dic[s[i]][0] + 1:
				res += dic[s[i+1]][1] - dic[s[i]][1]
				i += 2
			else:
				res += dic[s[i]][1]
				i += 1
		if i != n:
			res += dic[s[n-1]][1]
		return res

test = Solution()
print test.romanToInt('I'), 1
print test.romanToInt('III'), 3
print test.romanToInt('IV'), 4
print test.romanToInt('V'), 5
print test.romanToInt('VI'), 6
print test.romanToInt('VIII'), 8
print test.romanToInt('IX'), 9
print test.romanToInt('X'), 10
print test.romanToInt('CMXC'), 990
print test.romanToInt('CMXCIX'), 999
print test.romanToInt('MCMXCIX'), 1999
print test.romanToInt('MMX'), 2010
print test.romanToInt('MMXIX'), 2019