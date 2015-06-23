class Solution:
	# @param {string} s
	# @param {string} t
	# @return {integer}
	def numDistinct(self, s, t):
		ls = len(s)
		lt = len(t)
		a = [0 for i in range(lt+1)]
		a[0] = 1
		for i in range(ls):
			for j in range(lt, 0, -1):
				if s[i] == t[j-1]:
					a[j] += a[j-1]
			print a
		return a[lt]

test = Solution()
print test.numDistinct("", "")
print test.numDistinct("abcde", "ace")
print test.numDistinct("abcde", "aec")