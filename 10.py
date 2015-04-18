class Solution:

	def selfMatch(self, s, p):
		if s == p:
			return True
		if len(p) == 0 and len(s) > len(p):
			return False
		if len(p) == 1 and len(s) > len(p):
			return False
		if len(s) == 0 and len(p) % 2 != 0:
			return False
		if len(s) == 0 and p[1] == '*':
			return self.selfMatch(s, p[2: len(p)])
		if len(s) == 0 and p[1] != '*':
			return False
		if len(p) == 1 and (s[0] == p[0] or p[0] == '.'):
			return True

		while len(p) > 3 and p[1] == p[3] == '*':
			if p[0] == p[2]:
				p = p[2: len(p)]
			elif p[0] == '.' or p[2] == '.':
				p = '.' + p[3: len(p)]
			else:
				break

		if len(p) > 1:
			if p[0] == '*' and p[1] == '*':
				return False
			if p[0] == '.' and p[1] == '*':
				if self.selfMatch(s, p[2: len(p)]):
					return True
				else:
					return self.selfMatch(s[1: len(s)], p)
			if p[1] == '*':
				if len(s) == 0:
					return self.selfMatch(s, p[2: len(p)]);
				elif s[0] == p[0]:
					if self.selfMatch(s, p[2: len(p)]):
						return True
					else:
						return self.selfMatch(s[1: len(s)], p)
				else:
					return self.selfMatch(s, p[2: len(p)])

		if s[0] == p[0] or p[0] == '.':
			return self.selfMatch(s[1: len(s)], p[1: len(p)])
		else:
			return False

	def preSolve(self, s, p):
		i = len(p) - 1
		while i >= 0:
			if p[i] == '*':
				i -= 2
			elif p[i] == '.':
				i -= 1
			elif p[i] not in s:
				return True
			else:
				i -= 1
		else:
			return False

	# @param s, a string
	# @param p, a string
	# @return a boolean
	def isMatch(self, s, p):		
		if self.preSolve(s, p):
			return False
		else:
			return self.selfMatch(s, p)

test = Solution()
print test.isMatch("", ""), True
print test.isMatch("ab", ".*c"), False
print test.isMatch("aa", "a"), False
print test.isMatch("aa", "aa"), True
print test.isMatch("aa", "aaa"), False
print test.isMatch("aa", "a*"), True
print test.isMatch("aa", "a*a*"), True
print test.isMatch("aa", "a*a"), True
print test.isMatch("aa", "b*a"), False
print test.isMatch("aa", "a."), True
print test.isMatch("aa", ".*"), True
print test.isMatch("ab", ".*"), True
print test.isMatch("aab", "a*b"), True
print test.isMatch("aab", "c*a*b"), True
print test.isMatch("aab", "c*a*b*"), True
print test.isMatch("aab", "ac*a*b"), True
print test.isMatch("aab", "a*ab"), True
print test.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False
print test.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbb", "a*b*bc*c"), False
print test.isMatch("bbab", "b*a*"), False
print test.isMatch("bbbba", ".*a*a"), True
print test.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbb", "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*b*bc*c"), False
