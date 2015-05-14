class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def search(self, nums, target):
		n = len(nums)
		if n == 0:
			return -1
		if n == 1:
			if nums[0] == target:
				return 0
			else:
				return -1
		l = nums[0]
		r = nums[n-1]
		m = nums[(n-1) / 2]
		# print l,r,m		
		if target == l:
			return 0
		elif target == r:
			return n-1
		elif target == m:
			return (n-1) / 2
		if l < m and (l > target or target > m):
			f = self.search(nums[(n-1) / 2:n-1], target)
			if f == -1:
				return -1
			else:
				return (n-1) / 2 + f
		elif l < m:
			f = self.search(nums[0:(n-1) / 2], target)
			if f == -1:
				return -1
			else:
				return f
		elif l > m and (m > target or target > l):
			f = self.search(nums[0:(n-1) / 2], target)
			if f == -1:
				return -1
			else:
				return f
		elif l > m:
			f = self.search(nums[(n-1) / 2:n-1], target)
			if f == -1:
				return -1
			else:
				return (n-1) / 2 + f
		else:
			return -1


test = Solution()
print test.search([1,2,3,4,5,6], 4) == 3
print test.search([4,5,6,7,1,2,3], 1) == 4
print test.search([4,5,6,7,1,2,3], 5) == 1
print test.search([4,5,6,7,1,2,3], 2) == 5
print test.search([4,5,6,7,1,2,3], 6) == 2
print test.search([6,7,1,2,3,4,5], 1) == 2
print test.search([6,7,1,2,3,4,5], 8) == -1
print test.search([6,7,1,2,3,4,5], 7) == 1
print test.search([6,7,1,2,3,4,5], 4) == 5
print test.search([6,7,1,2,3,4,5], 3) == 4
print test.search([6,7,1,2,3,4,5], 2) == 3
print test.search([6,7,1,2,3,4,5], 5) == 6
print test.search([9,0,2,7,8], 3) == -1