class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def firstMissingPositive(self, nums):
		n = len(nums)
		if n <= 0:
			return 1
		i = 0
		while i < n:
			if nums[i] != i+1 and nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
				j = nums[i] - 1
				nums[i], nums[j] = nums[j], nums[i]
			else:
				i += 1
		# print nums
		for i in xrange(n):
			if nums[i] != i+1:
				return i+1
		return n+1

test = Solution()
print test.firstMissingPositive([1,5])
print test.firstMissingPositive([1,3,5,2])
print test.firstMissingPositive([1,-5,2])
print test.firstMissingPositive([3,4,-1,1])
print test.firstMissingPositive([1,1])