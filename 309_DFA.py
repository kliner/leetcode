class Solution(object):

    '''
    s0: waiting for buy
    s1: after buy, waiting for sell
    s2: after sell, need rest
    '''
    def maxProfit(self, prices):
        n = len(prices)
        s0, s1, s2 = [0]*n, [0]*n, [0]*n
        s1[0], s2[0] = -prices[0], -1e100
        for i in xrange(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s0[n-1], s2[n-1])

if __name__ == '__main__':
    test = Solution()
    print test.maxProfit([1,0,3])
    print test.maxProfit([1,2,3,0,2])
    print test.maxProfit([3,2,3,0,2,3])
