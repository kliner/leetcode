class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def majorityElement(self, nums):
		dct = {}
		l = len(nums)
		for n in nums:
			if n in dct:
				dct[n] += 1
				if dct[n] > l/2:
					return n
			else:
				dct[n]=1
				if dct[n] > l/2:
					return n

test = Solution()
print test.majorityElement([1])
print test.majorityElement([1,1,2])