class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		ss = s.split()[::-1]
		ans = ''
		for t in ss:
			ans += t + ' '
		return ans[:-1]

test = Solution()
print test.reverseWords("the sky is blue")