from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return -1
        total = sum(1 for i in xrange(m) for j in xrange(n) if grid[i][j] == 1)
        dists = [ [0]*n for i in xrange(m) ]
        cnts = [ [0]*n for i in xrange(m) ]

        def bfs(x0, y0):
            marked = [ [0]*n for i in xrange(m) ]
            q = deque()
            cnt = 1
            marked[x0][y0] = 1
            q.append((x0, y0, 0))
            while q:
                i, j, cur = q.popleft()
                dists[i][j] += cur
                for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=x<m and 0<=y<n and not marked[x][y]:
                        marked[x][y] = 1
                        cnts[x][y] += 1
                        if grid[x][y] == 0:
                            q.append((x, y, cur+1))
                        elif grid[x][y] == 1:
                            cnt += 1
            if cnt != total: return -1

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    if bfs(i, j): return -1
        
        aux = [dists[i][j] for i in xrange(m) for j in xrange(n) if grid[i][j] == 0 and cnts[i][j] == total] 
        if aux:
            return min(aux)
        else:
            return -1

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

