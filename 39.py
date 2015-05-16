import copy
class Solution:
	ans = []
	# @param {integer[]} candidates
	# @param {integer} target
	# @return {integer[][]}
	def combinationSum(self, candidates, target):
		self.ans = []
		candidates.sort()
		self.find([], candidates, target)
		return self.ans

	def find(self, cur, candidates, target):
		# print cur
		for i in xrange(len(candidates)):
			c = candidates[i]
			if c == target:
				cur.append(c)
				self.ans.append(copy.copy(cur))
				cur.pop()
				return
			elif c < target:
				cur.append(c)
				self.find(cur, candidates[i:], target - c)
				cur.pop()
			else:
				return

test = Solution()
print test.combinationSum([2,3,6,7],7)
print test.combinationSum([1,2,3,6,7],7)