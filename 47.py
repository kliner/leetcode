import copy
class Solution:
	ans = []
	# @param {integer[]} nums
	# @return {integer[][]}
	def permuteUnique(self, nums):
		self.ans = []
		nums.sort()
		l = len(nums)
		last = -98765432
		dic = {}
		for n in nums:
			if n == last:
				dic[n] += 1
			else:
				dic[n] = 1 
				last = n
		# print dic
		nums = dic.keys()
		self.solve(dic, nums, [], l)
		return self.ans

	def solve(self, dic, nums, a, l):
		if len(a) == l:
			self.ans.append(copy.copy(a))
			return
		# print dic
		for i in nums:
			if dic[i] > 0:
				a.append(i)
				dic[i] -= 1
				self.solve(dic, nums, a, l)
				dic[i] += 1
				a.pop()

test = Solution()
print test.permuteUnique([1,2,3])
print test.permuteUnique([1,2,1])
print test.permuteUnique([3,3,1,2,3,2,3,1])
print test.permuteUnique([-1,2,-1,2,1,-1,2,1])
print test.permuteUnique([1,2,2,1])