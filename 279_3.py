class Solution(object):

    # dp, n^1.5
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        dp = [0]
        while len(dp) <= n:
            cur = 1e10
            i = 1
            while i*i <= len(dp):
                cur = min(cur, dp[len(dp)-i*i]+1)
                i += 1
            dp.append(cur)
        return dp[n]

 
if __name__ == '__main__':
    test = Solution()
    print test.numSquares(1)
    print test.numSquares(12)
    print test.numSquares(13)
    print test.numSquares(3081)

