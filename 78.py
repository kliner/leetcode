import copy
class Solution:
	ans = []
	# @param {integer[]} nums
	# @return {integer[][]}
	def subsets(self, nums):
		self.ans = []
		nums.sort()
		self.dfs(nums, [])
		return self.ans

	def dfs(self, nums, cur):		
		self.ans.append(copy.copy(cur))
		for i in range(len(nums)):
			cur.append(nums[i])
			self.dfs(nums[i+1:], cur)
			cur.pop()

test = Solution()
print test.subsets([1,2,3])

