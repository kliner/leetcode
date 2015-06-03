class Solution:
	# @param {string} word1
	# @param {string} word2
	# @return {integer}
	def minDistance(self, word1, word2):
		if len(word1) > len(word2):
			word1, word2 = word2, word1
		l1 = len(word1)
		l2 = len(word2)
		if l1 == 0:
			return l2
		if l2 == 0:
			return l1
		m = []
		for i in range(l1+1):
			m.append([0 for i in range(l2+1)])
		for i in range(l1+1):
			m[i][0] = i
		for i in range(l2+1):
			m[0][i] = i
		for i in range(l1):
			for j in range(l2):
				if word1[i] == word2[j]:
					m[i+1][j+1] = m[i][j]
				else:
					m[i+1][j+1] = min(m[i][j], m[i+1][j], m[i][j+1]) + 1
		return m[l1][l2]

test = Solution()
print test.minDistance("a", "b")
print test.minDistance("abcd", "bcd")
print test.minDistance("distance", "springbok")
