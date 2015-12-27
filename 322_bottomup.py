class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        F = [-1 for i in xrange(amount+1)]
        F[0] = 0
        for i in xrange(1, amount+1):
            t = 1e10
            for coin in coins:
                #print i, coin, F[i-coin]
                if i-coin >= 0 and F[i-coin] != -1:
                    t = min(t, F[i-coin]+1)
            if t == 1e10:
                F[i] = -1
            else:
                F[i] = t
            #print F
            
        return F[-1]

    
if __name__ == '__main__':
    test = Solution()
    print test.coinChange([1,3,4,5], 7)
    print test.coinChange([112,149,215,496,482,436,144,397,500,189],8480)
