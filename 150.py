class Solution:
	# @param {string[]} tokens
	# @return {integer}
	def evalRPN(self, tokens):
		op = ['+', '-', '*', '/']
		stack = []
		for i in tokens:
			if i in op:
				b = stack.pop()
				a = stack.pop()
				if i == '+':
					stack.append(a+b)
				elif i == '-':
					stack.append(a-b)
				elif i == '*':
					stack.append(a*b)
				elif i == '/':
					t = a / b
					y = a % b
					if t < 0 and y != 0:
						t += 1
					stack.append(t)
			else:
				stack.append(int(i))
			# print stack
		return stack.pop()

test = Solution()
# print test.evalRPN(["2", "1", "+", "3", "*"])
# print test.evalRPN(["4", "13", "5", "/", "+"])
print test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])