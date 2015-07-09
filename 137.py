class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def singleNumber(self, nums):
		a = [0 for i in range(32)]
		b = [0 for i in range(32)]
		for n in nums:
			if n < 0:
				s = bin(n)[::-1][:-3]
				for i in range(len(s)):
					b[i] += int(s[i])

			else:
				s = bin(n)[::-1][:-2]
				for i in range(len(s)):
					a[i] += int(s[i])

		ans = 0
		t = [1]
		for i in range(31):
			t.append(t[-1] * 2)

		for i in range(32):
			ans += t[i] * (a[i] % 3)
			ans -= t[i] * (b[i] % 3)
		return ans


test = Solution()
print test.singleNumber([1,2,1,2,1,2,3,3,3,4])
print test.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])