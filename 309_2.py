class Solution(object):

    # bottom-up
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
            
        sell, buy, prevsell, prevbuy = 0, -prices[0], 0, 0
        for num in prices:
            prevbuy = buy
            buy = max(prevsell - num, buy)
            prevsell = sell
            sell = max(prevbuy + num, sell)
        return sell


if __name__ == '__main__':
    test = Solution()
    print test.maxProfit([1,3])
    print test.maxProfit([1,0,3])
    print test.maxProfit([1,2,3,0,2])
    print test.maxProfit([3,2,3,0,2,3])


