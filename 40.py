import copy
class Solution:
	ans = {}
	# @param {integer[]} candidates
	# @param {integer} target
	# @return {integer[][]}
	def combinationSum2(self, candidates, target):
		self.ans = {}
		candidates.sort()
		self.find([], candidates, target)
		res = []
		for i in self.ans.keys():
			l = i.split(',')
			t = []
			for j in xrange(len(l) - 1):
				t.append(int(l[j]))
			res.append(t)
		return res

	def find(self, cur, candidates, target):
		# print cur
		for i in xrange(len(candidates)):
			c = candidates[i]
			if c == target:
				cur.append(c)
				s = ''
				for x in cur:
					s += `x` + ','
				if s not in self.ans:
					self.ans[s] = 1
				cur.pop()
				return
			elif c < target:
				cur.append(c)
				self.find(cur, candidates[i+1:], target - c)
				cur.pop()
			else:
				return

test = Solution()
print test.combinationSum2([10,1,2,7,6,1,5],8)
print test.combinationSum2([1,2,3,6,7],7)
print test.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)