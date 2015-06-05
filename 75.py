class Solution:
	# @param {integer[]} nums
	# @return {void} Do not return anything, modify nums in-place instead.
	def sortColors(self, nums):
		n = len(nums)
		l = 0
		r = n-1
		c = 0
		for i in range(n):
			if nums[c] == 0:
				nums[l], nums[c] = nums[c], nums[l]
				l += 1
				c += 1
			elif nums[c] == 2:
				nums[r], nums[c] = nums[c], nums[r]
				r -= 1
			else:
				c += 1
			
test = Solution()
a = [1,2,1,0]
test.sortColors(a)
print a
a = [2,1,0,2,1,0]
test.sortColors(a)
print a