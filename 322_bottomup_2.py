class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        F = [None for i in xrange(amount+1)]
        F[0] = 0
        cnt = amount / min(coins)
        nxt = set([0])
        
        for i in xrange(cnt):
            reached = nxt
            nxt = set([])
            for val in reached:
                for coin in coins:
                    if val+coin > amount:
                        continue
                    if F[val+coin] == None:
                        F[val+coin] = F[val] + 1
                    else:
                        F[val+coin] = min(F[val+coin], F[val]+1)
                    nxt.add(val+coin)
                        
        if F[-1]:
            return F[-1]
        else:
            return -1

    

if __name__ == '__main__':
    test = Solution()
    print test.coinChange([1,3,4,5], 7)
    print test.coinChange([112,149,215,496,482,436,144,397,500,189],8480)


