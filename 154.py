class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def findMin(self, nums):
		n = len(nums)
		if n == 0:
			return 0
		if n == 1:
			return nums[0]
		l = 0
		r = n - 1
		while l < r:
			print nums[l:r+1]
			t = (l+r) >> 1
			if nums[l] < nums[t] and nums[l] < nums[r]:
				return nums[l]
			if r == l+1:	
				return min(nums[l], nums[r])

			tt = t
			if nums[l] == nums[tt]:
				while tt <= r and nums[l] == nums[tt]:
					tt += 1
				if tt == r + 1:
					r = t
					continue
				else:
					l = t
					continue

			if nums[t] > nums[l]:
				l = t
			else:
				r = t
		return nums[l]

test = Solution()
# print test.findMin([6,7,1,2,3,4,5])
# print test.findMin([4,5,6,7,1,2,3])
# print test.findMin([1,2,3,4,5,6,7])
# print test.findMin([2,3,4,5,6,7,1])
# print test.findMin([1,1,1,1,1])
# print test.findMin([1,1,1,1,4])
# print test.findMin([4,1,1,1,1])
# print test.findMin([1,1,1,4,1])
# print test.findMin([1,1,4,1,1])
# print test.findMin([1,4,1,1,1])
print test.findMin([0,0,1,1,2,0])
print test.findMin([1])