class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def longestConsecutive(self, nums):
		if len(nums) == 0:
			return 0
		dct = dict(zip(nums, [0 for n in nums]))
		ans = 1
		while len(dct) != 0:
			cnt = 1
			i = dct.keys()[0]
			dct.pop(i)
			next = i+1
			while next in dct:
				dct.pop(next)
				cnt += 1
				next += 1
			prev = i-1
			while prev in dct:
				dct.pop(prev)
				cnt += 1
				prev -= 1
			ans = max(ans, cnt)
		return ans

test = Solution()
# print test.longestConsecutive([])
# print test.longestConsecutive([1,2,3,4,100,200])
# a = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
# a.sort()
# print a
print test.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
