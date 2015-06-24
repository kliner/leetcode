class Solution:
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, prices):
		if len(prices) <= 1:
			return 0
		inPrice = prices[0]
		outPrice = prices[0]
		profit = 0
		for p in prices:
			if p < inPrice:
				inPrice = p
				outPrice = p
			if p > outPrice:
				outPrice = p
				profit = max(profit, outPrice - inPrice)
		return profit

test = Solution()
print test.maxProfit([1,2,3,2,6])
print test.maxProfit([5,3,6,1,5])