class Solution:
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, prices):
		n = len(prices)
		if n == 0:
			return 0
		a = [0 for i in range(n)]
		b = [0 for i in range(n)]
		mina = 9999999999999999L
		pro = 0
		for i in range(n):
			if prices[i] < mina:
				mina = prices[i]
			else:
				pro = max(prices[i] - mina, pro)
			a[i] = pro
		maxb = -9999999999999999L
		pro = 0
		for i in range(n-1, -1, -1):
			if prices[i] > maxb:
				maxb = prices[i]
			else:
				pro = max(maxb - prices[i], pro)
			b[i] = pro
		return max([a[i]+b[i] for i in range(n)])

test = Solution()
print test.maxProfit([1,5,2,3,2,4])
			


