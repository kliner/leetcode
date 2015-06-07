class Solution:
	# @param {integer[]} nums1
	# @param {integer} m
	# @param {integer[]} nums2
	# @param {integer} n
	# @return {void} Do not return anything, modify nums1 in-place instead.
	def merge(self, nums1, m, nums2, n):
		p1 = m-1
		p2 = n-1
		if p2 < 0:
			return 
		for i in range(m + n - 1, -1, -1):
			if p1 < 0 or (nums1[p1] < nums2[p2] and p2 >= 0):
				nums1[i] = nums2[p2]
				i -= 1
				p2 -= 1
			else:
				nums1[i] = nums1[p1]
				i -= 1
				p1 -= 1

test = Solution()
a = [1,3,5,0,0]
b = [2,4]
test.merge(a, 3, b, 2)
print a
