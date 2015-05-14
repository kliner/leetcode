class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def searchRange(self, nums, target):
		a = []
		a.append(self.searchL(nums, target))
		a.append(self.searchR(nums, target))
		return a
		
	def searchL(self, nums, target):
		if len(nums) == 0:
			return -1
		if len(nums) == 1:
			if target == nums[0]:
				return 0
			else:
				return -1
		l = 0
		r = len(nums) - 1
		m = (l + r) / 2
		if nums[l] == target:
			return l
		if nums[r] == target and r > l and nums[r-1] < target:
			return r
		if nums[m] == target and m > l and nums[m-1] < target:
			return m
		if target <= nums[m]:
			return self.searchL(nums[0:m], target)
		if target > nums[m]:
			f = self.searchL(nums[m:r], target)
			if f == -1:
				return f
			else:
				return f + m
		return -1

	def searchR(self, nums, target):
		if len(nums) == 0:
			return -1
		if len(nums) == 1:
			if target == nums[0]:
				return 0
			else:
				return -1
		l = 0
		r = len(nums) - 1
		m = (l + r) >> 1
		# print nums[l],nums[m],nums[r]
		if nums[l] == target and ( (r > l and nums[l+1] > target) or r == l ):
			return l
		if nums[r] == target:
			return r
		if nums[m] == target and ( (r > m and nums[m+1] > target) or r == m ):
			return m

		# print nums[m], target
		if target < nums[m]:
			return self.searchR(nums[0:m], target)
		if target >= nums[m]:
			f = self.searchR(nums[m:r], target)
			if f == -1:
				return f
			else:
				return f + m
		return -1

test = Solution()
print test.searchRange([1,1,1,1,1,1,1,1,1,1,1,1,1], 1) 
print test.searchRange([1,1,1,1,1,1,1,1,1,1,1,1,1], 2) 
print test.searchRange([1,2,3,3,3,4,5,6,7,8,9], 3)
print test.searchRange([1,2,3,3,3,4,5,6,7,8,9], 6)
print test.searchRange([1,2,3,3,3,4,5,6,7,8,9], 9)
print test.searchRange([0,0,1,1,1,2,4,4,4,4,5,5,5,6,8,8,9,9,10,10,10], 8)