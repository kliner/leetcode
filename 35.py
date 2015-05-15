class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def searchInsert(self, nums, target):
		l = 0
		r = len(nums)-1
		m = l + r >> 1
		if nums[l] >= target:
			return l
		if nums[r] == target:
			return r
		if nums[r] <= target:
			return r+1
		if nums[m] == target:
			return m
		if target > nums[m]:
			return m + self.searchInsert(nums[m:r], target)
		else:
			return self.searchInsert(nums[l:m], target)

test = Solution()
print test.searchInsert([1,3,5,6], 5)
print test.searchInsert([1,3,5,6], 2)
print test.searchInsert([1,3,5,6], 7)
print test.searchInsert([1,3,5,6], 0)
print test.searchInsert([1,2,3,4,5,7,8], 6)
print test.searchInsert([1,2,3,4,5,7,8], 7)
print test.searchInsert([1,2,4,5,7,8,10,12,13,16,17], 10)
print test.searchInsert([1,2,4,5,7,8,10,12,13,16,17], 14)