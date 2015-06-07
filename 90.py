import copy
class Solution:
	ans = []
	# @param {integer[]} nums
	# @return {integer[][]}
	def subsetsWithDup(self, nums):
		self.ans = []
		nums.sort()
		self.dfs(nums, [])
		return self.ans

	def dfs(self, nums, s):
		self.ans.append(copy.copy(s))
		last = 'h'
		for i in range(len(nums)):
			if nums[i] == last:
				continue
			last = nums[i]
			s.append(nums[i])
			self.dfs(nums[i+1:], s)
			s.pop()

test = Solution()
print test.subsetsWithDup([0])
print test.subsetsWithDup([1,2,2])