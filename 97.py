class Solution:
	# @param {string} s1
	# @param {string} s2
	# @param {string} s3
	# @return {boolean}
	def isInterleave(self, s1, s2, s3):
		l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		if l1 + l2 != l3:
			return False
		if l1 == 0:
			return s2 == s3        		
		if l2 == 0:
			return s1 == s3
		if l3 == 0:
			return l1 + l2 == 0
		a = []
		for i in range(l1+1):
			a.append([0 for i in range(l2+1)])
		for i in range(l1):
			if s1[i] == s3[i]:
				a[i+1][0] = 1
			else:
				break
		for i in range(l2):
			if s2[i] == s3[i]:
				a[0][i+1] = 1
			else:
				break
		for i in range(l1):
			for j in range(l2):
				# print s1[i], s2[j], s3[i+j], a[i][j+1], a[i+1][j]
				if (s1[i] == s3[i+j+1] and a[i][j+1] == 1) or (s2[j] == s3[i+j+1] and a[i+1][j] == 1):
					a[i+1][j+1] = 1
					# print a[i+1][j+1]
		# print a
		if a[l1][l2] == 1:
			return True
		else:
			return False

test = Solution()
print test.isInterleave("a", "", "a") == True
print test.isInterleave("a", "a", "aa") == True
print test.isInterleave("ab", "ba", "aabb") == False
print test.isInterleave("ab", "ba", "abba") == True
print test.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
print test.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False