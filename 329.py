class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        if not n:
            return 0
        m = len(matrix[0])
        if not m:
            return 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        dp = [[0] * m for i in xrange(n)]

        def dfs(x,y):
            if dp[x][y]:
                return dp[x][y]
            dp[x][y] = 1
            for i in xrange(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and matrix[nx][ny] < matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
            return dp[x][y]

        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                ans = max(ans, dfs(i,j))
        return ans
            
test = Solution()
print test.longestIncreasingPath(None)
print test.longestIncreasingPath([])
print test.longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
])
print test.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
])

