class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		if len(s) == 0:
			return 0
		a = [1]
		for i in range(1, len(s)):
			j = a[i-1]
			try:
				k = s[i-j:i].index(s[i])
				a.append(j-k)
			except Exception, e:
				a.append(j+1)
		return max(a)

test = Solution()
print test.lengthOfLongestSubstring("")