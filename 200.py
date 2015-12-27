class Solution(object):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        self.m = m
        self.n = n

        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt
        
    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        for t in range(4):
            x = i + self.dx[t]
            y = j + self.dy[t]
            if x >= 0 and x < self.m and y >= 0 and y < self.n and grid[x][y] == '1':
                self.dfs(grid, x, y)
        
if __name__ == '__main__':
    test = Solution()
    print test.numIslands([
        ['1','0'],
        ['1','1']
        ])
