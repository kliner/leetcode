class Solution:
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, prices):
		cur = 99999999999999999L
		ans = 0
		for p in prices:
			if p > cur:
				ans += (p - cur)
			cur = p
		return ans

test = Solution()
print test.maxProfit([1,2,3,4,5])
print test.maxProfit([1,5,2,4,3,6]) 