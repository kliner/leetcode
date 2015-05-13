class Solution:
	# @param {string} s
	# @return {integer}
	def longestValidParentheses(self, s):
		n = len(s)
		if n <= 1:
			return 0
		a = []		
		for i in range(n):
			if s[i] == '(':
				a.append(0)
			elif s[i] == ')':
				if i == 1 and s[i - 1] == '(':
					a.append(2)
				elif i > 1 and s[i - 1] == '(':
					a.append(a[i - 2] + 2)
				elif i > 1 and i == a[i-1] + 1 and s[i - 1] == ')' and s[i - a[i-1] - 1] == '(':
					a.append(a[i - 1] + 2)
				elif i > 1 and i > a[i-1] + 1 and s[i - 1] == ')' and s[i - a[i-1] - 1] == '(':
					a.append(a[i - 1] + 2 + a[i - a[i-1] - 2])
				else:
					a.append(0)
		return max(a)

test = Solution()
print test.longestValidParentheses(")")
print test.longestValidParentheses(")(")
print test.longestValidParentheses("))))))))(((((")
print test.longestValidParentheses("))))))))((((()))))))))))))))))))))(((((((((((((((((")
print test.longestValidParentheses("))))))))((((()))))))))))))))))))))((((((((((((((((())))))))")
print test.longestValidParentheses("(()")
print test.longestValidParentheses("()()")
print test.longestValidParentheses("(())(())")
print test.longestValidParentheses("(())(())(())(())")
print test.longestValidParentheses("(())(((())(())(((())")
print test.longestValidParentheses("())()))()())()((())))())()))(()))))(()()))())(()))()))()()))((()))()((()()))))()((())())(((((()(())(((")