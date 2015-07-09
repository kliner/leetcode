class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def singleNumber(self, nums):
		ans = 0
		for n in nums:
			ans ^= n
		return ans

test = Solution()
print test.singleNumber([1,2,3,2,1])