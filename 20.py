class Solution:
	# @param {string} s
	# @return {boolean}
	def isValid(self, s):
		stack = []
		for i in s:
			if i in ['{', '(', '[']:
				stack.append(i)
			elif i in ['}', ')', ']']:
				if len(stack) == 0:
					return False
				j = stack.pop()
				if (i == '}' and j == '{') or (i == ')' and j == '(') or (i == ']' and j == '['):
					continue
				else:
					return False
			else:
				return False
		if len(stack) == 0:
			return True
		else:
			return False

test = Solution()
print test.isValid("")
print test.isValid("()[]{}")
print test.isValid("()()()")
print test.isValid("([{()}])")
print test.isValid("([{(}{()")
print test.isValid("(]")

