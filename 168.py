class Solution:
	# @param {integer} n
	# @return {string}
	def convertToTitle(self, n):
		if n == 0:
			return ""
		ans = ""
		while n != 0:
			t = n % 26
			if t == 0:
				t = 26
				n = n / 26 - 1
			else:
				n = n / 26
			ans = chr(ord('A') + t - 1) + ans
			
		return ans

test = Solution()
print test.convertToTitle(0)
print test.convertToTitle(1)
print test.convertToTitle(26)
print test.convertToTitle(27)
print test.convertToTitle(28)
print test.convertToTitle(27*26)
print test.convertToTitle(27*26+1)