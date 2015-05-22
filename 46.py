import copy
class Solution:
	ans = []
	# @param {integer[]} nums
	# @return {integer[][]}
	def permute(self, nums):
		self.ans = []
		self.solve(nums, [], len(nums))
		return self.ans

	def solve(self, nums, a, n):
		# print nums, a, n
		if n == len(a):
			self.ans.append(copy.copy(a))
			return
		for i in range(len(nums)):
			a.append(nums[i])
			self.solve(nums[:i]+nums[i+1:], a, n)
			a.remove(nums[i])

test = Solution()
print test.permute([1,2,3])

