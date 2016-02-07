class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n or not k: return 0
        if n == 1: return k
        if k == 1:
            if n > 2: return 0
            else: return 1
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in xrange(2,n):
            dp[i] = (dp[i-1]+dp[i-2])*(k-1)
    
        return dp[n-1]

test = Solution()
print test.numWays(0,1) == 0
print test.numWays(1,0) == 0
print test.numWays(1,1) == 1
print test.numWays(1,2) == 2
print test.numWays(1,3) == 3
print test.numWays(2,1) == 1
print test.numWays(3,1) == 0
print test.numWays(2,2) == 4
print test.numWays(3,2) == 6
print test.numWays(2,3) == 9
print test.numWays(3,3) == 24
