from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return -1
        total = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    total += 1
        dists = [[0]*n for i in xrange(m)]
        cnts = [[0]*n for i in xrange(m)]

        def bfs(x0, y0):
            visit = [[0]*n for i in xrange(m)]
            cnt = 1
            q = deque()
            q.append((x0,y0,0))
            visit[x0][y0] = 1
            while q:
                x, y, d = q.popleft()
                for i, j in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
                    if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                        if grid[i][j] == 0:
                            q.append((i,j,d+1))
                            dists[i][j] += d+1
                            cnts[i][j] += 1
                        elif grid[i][j] == 1:
                            cnt += 1
                        visit[i][j] = 1
            return cnt

        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1:
                    cnt = bfs(x,y)
                    if cnt != total: return -1
        t = [dists[i][j] for i in xrange(m) for j in xrange(n) if cnts[i][j] == total]
        if not t:
            return -1
        return min(t)

test = Solution()
print test.shortestDistance([
    [1]
    ])
print test.shortestDistance([
    [1,0]
    ])
print test.shortestDistance([
    [1,1]
    ])
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

