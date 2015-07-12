class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def maxProduct(self, nums):
		n = len(nums)
		if n == 0:
			return 0
		if n == 1:
			return nums[0]

		if nums[0] > 0:
			a = [(nums[0], 0)]
		else:
			a = [(0, nums[0])]

		for i in range(1, n):
			if nums[i] > 0:
				a.append((max(a[-1][0] * nums[i], nums[i]), min(a[-1][1] * nums[i], 0)))
			else:
				a.append((max(a[-1][1] * nums[i], 0), min(a[-1][0] * nums[i], nums[i])))
		b = 0
		for i in range(n):
			b = max(b, a[i][0])
		return b

test = Solution()
print test.maxProduct([2,3,-2,4])