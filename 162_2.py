class Solution:
	# @param nums, an integer[]
	# @return an integer
	def findPeakElement(self, nums):
		n = len(nums)
		l, r = 0, n-1
		while l <= r:
			m = (l+r) >> 1
			if l == r:
				return l
			if nums[m]<nums[m+1]:
				l = m+1
			else:
				r = m

test = Solution()
print test.findPeakElement([1,2,3,1])
print test.findPeakElement([1,2,3])
print test.findPeakElement([3,1])