class Solution:
	def solve(self, cur, n, stk, res, ans):
		if cur == n and len(res) == n * 2:
			ans.append(res)
			return
		if stk > 0:
			stk -= 1
			self.solve(cur, n, stk, res + ")", ans)
			stk += 1
		if cur < n:
			cur += 1
			stk += 1
			self.solve(cur, n, stk, res + "(", ans)
			stk -= 1
			cur -= 1


	# @param {integer} n
	# @return {string[]}
	def generateParenthesis(self, n):
		ans = []
		self.solve(0, n, 0, "", ans)
		return ans

test = Solution()
print test.generateParenthesis(2)
print test.generateParenthesis(3)
print len(test.generateParenthesis(4)) == 14