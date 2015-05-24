class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def maxSubArray(self, nums):
		n = len(nums)
		a = [nums[i] for i in range(n)]
		for i in range(1, n):
			if a[i-1] > 0:
				a[i] = a[i-1] + nums[i]
		return max(a)

test = Solution()
print test.maxSubArray([1,2,3,4,5])
print test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])