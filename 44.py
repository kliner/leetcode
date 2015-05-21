class Solution:
	# @param {string} s
	# @param {string} p
	# @return {boolean}
	def isMatch(self, s, p):
		# print s, p
		l1 = len(s)
		l2 = len(p)
		if (l1 == 0 and l2 == 0) or (l1 == 1 and l2 == 1 and p[0] == '?') or (l1 == 1 and l2 == 1 and p[0] == '*') or (l1 == 1 and l2 == 1 and s[0] == p[0]):
			return True
		elif l1 > 0 and l2 == 0:
			return False
		# elif p[0] == '*':
		# 	while p[0] == '*':
		# 		if len(p) == 1:
		# 			return True
		# 		p = p[1:]
		# 	for i in xrange(l1):
		# 		if self.isMatch(s[i:], p):
		# 			return True
		# 	return False
		# elif l1 > 0 and (s[0] == p[0] or p[0] == '?'):
		# 	return self.isMatch(s[1:], p[1:])
		# else:
		# 	return False
		firstf = False
		endf = False
		if p[0] != '*':
			firstf = True
		if p[l2-1] != '*':
			endf = True
		ps = p.split('*')
		while '' in ps:
			ps.remove('')
		# print ps
		for i in xrange(len(ps)):
			# print s, ps[i]
			t = self.find(s, ps[i])
			# print t
			if i == 0 and firstf:
				if t != 0:
					return False
			elif i == len(ps)-1 and endf:
				t = self.find(s[len(s)-len(ps[i]):], ps[i])
				if t != 0:
					return False
				else:
					return True
			if t == -1:
				return False
			s = s[t+len(ps[i]):]
		if firstf and endf and len(s) > 0:
			return False
		else:
			return True

	def find(self, s, p):
		for i in xrange(len(s)-len(p)+1):
			f = True
			for j in xrange(len(p)):
				if s[i+j] != p[j] and p[j] != '?':
					f = False
			if f:
				return i
		return -1


test = Solution()
print test.isMatch("aa","a") == False
print test.isMatch("aa","aa") == True
print test.isMatch("aa","*aa") == True
print test.isMatch("aaa","aa") == False
print test.isMatch("aa", "*") == True
print test.isMatch("aa", "a*") == True
print test.isMatch("ab", "?*") == True
print test.isMatch("aab", "c*a*b") == False
print test.isMatch("ab", "*?") == True
print test.isMatch("ba", "*") == True
print test.isMatch("ba", "??") == True
print test.isMatch("ba", "???") == False
print test.isMatch("", "") == True
print test.isMatch("a", "") == False
print test.isMatch("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab", "*babbbb*aab**b*bb*aa*") == True
print test.isMatch("abbbabaaabbabbabbabaabbbaabaaaabbbabaaabbbbbaaababbb", "**a*b*aa***b***bbb*ba*a") == False
print test.isMatch("abefcdgiescdfimde", "ab*cd?i*de") == True