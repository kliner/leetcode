class Solution:
	# @param {string[]} strs
	# @return {string}
	def longestCommonPrefix(self, strs):
		n = len(strs)
		if n == 0:
			return ''
		a = strs[0]
		for i in xrange(len(a)):
			for j in xrange(1, n):
				if len(strs[j]) == i:
					return a[:i]
				if strs[j][i] != a[i]:
					return a[:i]
		return a

test = Solution()
print test.longestCommonPrefix([]) == ''
print test.longestCommonPrefix(['', 'ab', 'ac']) == ''
print test.longestCommonPrefix(['a', '', 'c']) == ''
print test.longestCommonPrefix(['a', 'ab', 'ac']) == 'a'
print test.longestCommonPrefix(['g', 'gab', 'gac']) == 'g'
print test.longestCommonPrefix(['gabc', 'g', 'gac']) == 'g'
print test.longestCommonPrefix(['gabc', 'gacb', 'gac']) == 'ga'
print test.longestCommonPrefix(['gab', 'gab', 'gac']) == 'ga'