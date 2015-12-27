class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNums = [1]
        for num in nums:
            if num:
                myNums.append(num)
        myNums.append(1)
        n = len(myNums)
        F = [[0] * n for i in xrange(n)]
        for i in xrange(1,n-1):
            F[i-1][i+1] = myNums[i-1]*myNums[i]*myNums[i+1]
        for i in xrange(2,n):
            for start in xrange(0, n-i):
                end = start + i
                for k in xrange(start+1, end):
                    F[start][end] = max(F[start][end], F[start][k] + F[k][end] + myNums[start]*myNums[k]*myNums[end])
        return F[0][n-1]


if __name__ == '__main__':
    test = Solution()
    print test.maxCoins([3,1,5,8])

