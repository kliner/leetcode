class Solution(object):

    # dp, n^1.5 * cnt
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        a = [1]
        while a[-1] < n:
            i+=1
            a.append(i**2)
        dp = [1e10 for i in xrange(n+1)]
        dp[0] = 0
        while dp[n] == 1e10:
            for i in xrange(n):
                if dp[i] != 1e10:
                    for j in a:
                        if i+j <= n:
                            dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[n]

 
if __name__ == '__main__':
    test = Solution()
    print test.numSquares(12)
    print test.numSquares(13)
    print test.numSquares(3081)
