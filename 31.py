class Solution:
	def swap(self, nums, i, j):
		t = nums[i];
		nums[i] = nums[j];
		nums[j] = t;

	# @param {integer[]} nums
	# @return {void} Do not return anything, modify nums in-place instead.
	def nextPermutation(self, nums):
		n = len(nums)
		if n <= 1:
			return
		for i in range(n-1, 0, -1):
			if nums[i] > nums[i-1]:
				i -= 1
				break
		else:
			for i in range(n/2):
				self.swap(nums, i, n-1-i)
			return

		for j in range(n-1, i, -1):
			if nums[i] < nums[j]:
				break

		if i >= 0:
			self.swap(nums, i, j)
			nums[i+1:n] = nums[n-1:i:-1]
		# print nums
		

test = Solution()
a = [1, 2, 3]
test.nextPermutation(a)
print a == [1, 3, 2]
a = [1, 3, 2]
test.nextPermutation(a)
print a == [2, 1, 3]
a = [2, 1, 3]
test.nextPermutation(a)
print a == [2, 3, 1]
a = [2, 3, 1]
test.nextPermutation(a)
print a == [3, 1, 2]
a = [3, 1, 2]
test.nextPermutation(a)
print a == [3, 2, 1]
a = [3, 2, 1]
test.nextPermutation(a)
print a == [1, 2, 3]
a = [1, 4, 3, 2]
test.nextPermutation(a)
print a == [2, 1, 3, 4]
a = [2, 4, 3, 1]
test.nextPermutation(a)
print a == [3, 1, 2, 4]
a = [3, 4, 2, 1]
test.nextPermutation(a)
print a == [4, 1, 2, 3]
a = [4, 1, 3, 2]
test.nextPermutation(a)
print a == [4, 2, 1, 3]
a = [5,4,7,5,3,2]
test.nextPermutation(a)
print a == [5,5,2,3,4,7]
a = [4,2,0,2,3,2,0]
test.nextPermutation(a)
print a == [4,2,0,3,0,2,2]