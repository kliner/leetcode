class Solution:
	# @param {integer[]} height
	# @return {integer}
	def largestRectangleArea(self, height):
		n = len(height)
		if n == 0:
			return 0
		stack = []
		height.append(0)
		ans = 0
		for i in range(n+1):
			if len(stack) == 0 or height[i] > height[stack[-1]]:
				stack.append(i)
			else:
				while height[stack[-1]] > height[i] and len(stack) > 0:
					t = stack.pop()
					if len(stack) == 0:
						ans = max(ans, height[t] * i)
						# print stack, ans
						break
					else:
						ans = max(ans, height[t] * (i - stack[-1] - 1))
						# print stack, ans
				stack.append(i)

		return ans

test = Solution()
print test.largestRectangleArea([4,2,0,3,2,5])
print test.largestRectangleArea([2,1,5,6,2,3])