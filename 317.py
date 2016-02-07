from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        total = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    total += 1
        cnts = [[-1]*n for i in xrange(m)]

        def bfs(x0, y0):
            visit = [[0]*n for i in xrange(m)]
            cnt = 0
            dist = 0
            q = deque()
            q.append((x0,y0,0))
            visit[x0][y0] = 1
            while q:
                x, y, d = q.popleft()
                for i, j in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
                    if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                        if cnts[i][j] != -1 and cnts[i][j] < total:
                            cnts[x0][y0] = 0
                            return 
                        if grid[i][j] == 0:
                            q.append((i,j,d+1))
                        elif grid[i][j] == 1:
                            cnt += 1
                            dist += d+1
                        visit[i][j] = 1

            cnts[x0][y0] = cnt
            if cnt == total:
                return dist

        ans = 1e100
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 0:
                    candi = bfs(x,y)
                    if candi: ans = min(ans, candi)
        if ans == 1e100: return -1 
        else: return ans

test = Solution()
print test.shortestDistance([
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
    ])
print test.shortestDistance([
    [1,0,2,0,1],
    [0,2,0,0,0],
    [0,2,1,0,0]
    ])
print test.shortestDistance([
    [1,1,1,0,1],
    [0,0,1,0,0],
    [1,0,1,0,0]
    ])
print test.shortestDistance([
    [0,0,0,0,1],
    [1,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
    ])
