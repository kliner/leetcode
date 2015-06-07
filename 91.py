class Solution:
	# @param {string} s
	# @return {integer}
	def numDecodings(self, s):
		n = len(s)
		if n == 0 or s[0] == '0':
			return 0
		if n == 1:
			return 1
		a = [1 for i in range(n)]
		for i in range(1, n):
			if s[i] == '0':
				if s[i-1] == '1' or s[i-1] == '2':
					a[i] = a[i-2]
				else:
					return 0
			elif s[i-1] == '1' or (s[i-1] == '2' and s[i] in ['0','1','2','3','4','5','6']):
				if i == 1:
					a[i] = a[i-1] + 1
				else:
					a[i] = a[i-2] + a[i-1]
			else:
				a[i] = a[i-1]
		return a[n-1]

test = Solution()
print test.numDecodings("1") == 1
print test.numDecodings("11") == 2
print test.numDecodings("33") == 1
print test.numDecodings("30") == 0
print test.numDecodings("310")
print test.numDecodings("210")
print test.numDecodings("23") == 2
print test.numDecodings("112") == 3

# 112
# 1,1,1
# 11,2
# 1,12