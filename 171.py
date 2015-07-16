class Solution:
	# @param {string} s
	# @return {integer}
	def titleToNumber(self, s):
		ans = 0
		if s == '':
			return ans
		for ch in s:
			ans = ans * 26 + ord(ch) - ord('A') + 1
		return ans

test = Solution()
print test.titleToNumber('')
print test.titleToNumber('A')
print test.titleToNumber('Z')
print test.titleToNumber('AA')
print test.titleToNumber('AZ')
print test.titleToNumber('ZZ')
