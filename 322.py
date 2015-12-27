class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        F = [None for i in xrange(amount+1)]
        F[0] = 0
        return self.dp(coins, amount, F)
        
        
    def dp(self, coins, n, F):
        #print n
        if F[n] is not None:
            #print 'ret:', F[n]
            return F[n]
        ans = 1e10
        for coin in coins:
            if n-coin >= 0: 
                ans = min(ans, self.dp(coins, n-coin, F)+1 )
        F[n] = ans
        #print "ans:", ans
        return F[n]
    

if __name__ == '__main__':
    test = Solution()
    print test.coinChange([1,3,4,5], 7)
    print test.coinChange([112,149,215,496,482,436,144,397,500,189],8480)
