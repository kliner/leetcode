class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def canJump(self, nums):
		r = nums[0]
		i = 0
		n = len(nums)
		if n == 1:
			return True
		while i <= r:
			r = max(i + nums[i], r)
			i += 1
			if r >= n-1:
				return True
		return False

test = Solution()
print test.canJump([1,2,3])
print test.canJump([2,3,1,1,4])
print test.canJump([3,2,1,0,1])
