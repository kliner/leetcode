class Solution:
	# @param nums, an integer[]
	# @return an integer
	def findPeakElement(self, nums):
		n = len(nums)
		if n <= 1:
			return 0
		for i in range(1, n):
			if nums[i-1] > nums[i]:
				return i-1
		return n-1

test = Solution()
print test.findPeakElement([1,2,3,1])
print test.findPeakElement([1,2,3])
print test.findPeakElement([3,1])