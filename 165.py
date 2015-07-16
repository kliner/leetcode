class Solution:
	# @param {string} version1
	# @param {string} version2
	# @return {integer}
	def compareVersion(self, version1, version2):
		v1s = version1.split('.')
		v2s = version2.split('.')
		l1 = len(v1s)
		l2 = len(v2s)
		v1s = [int(v) for v in v1s]
		v2s = [int(v) for v in v2s]
		if l1 < l2:
			v1s.extend([0 for i in range(l2 - l1)])
			l1 = l2
		else:
			v2s.extend([0 for i in range(l1 - l2)])
			l2 = l1
		print v1s, v2s
		for i in range(l1):
			if v1s[i] < v2s[i]:
				return -1
			elif v1s[i] > v2s[i]:
				return 1
		return 0

test = Solution()
print test.compareVersion("1.0", "1")
print test.compareVersion("1.0", "1.1")
print test.compareVersion("11.0", "1.1")
print test.compareVersion("0.1", "1.1")