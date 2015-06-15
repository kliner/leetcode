class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def removeDuplicates(self, nums):
		second = False
		n = len(nums)
		if n == 0:
			return 0
		last = nums[0]
		ans = 1
		for i in range(1, n):
			if nums[i] != last:
				second = False
				last = nums[i]
				nums[ans], nums[i] = nums[i], nums[ans]
				ans += 1
			elif nums[i] == last and not second:
				second = True
				nums[ans], nums[i] = nums[i], nums[ans]
				ans += 1
		return ans

test = Solution()
a = [1,1,1,2,2,3]
print test.removeDuplicates(a), a
