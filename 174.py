class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        m = len(dungeon)
        if m <= 0:
            return 0
        n = len(dungeon[0])
        if n <= 0:
            return 0

        dp = [[1 for col in range(n)] for row in range(m)]
        dp[-1][-1] = max(1-dungeon[-1][-1], 1)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                elif i == m-1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 1)
                elif j == n-1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 1)
                else:
                    dp[i][j] = max(min(dp[i+1][j] - dungeon[i][j], dp[i][j+1] - dungeon[i][j]), 1)
        #print dp
        return dp[0][0]
                

if __name__ == '__main__':
    test = Solution()
    print test.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5] 
        ])

