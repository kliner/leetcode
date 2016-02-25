from collections import deque

INF = 2147483647

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0: return 
        n = len(rooms[0])
        if n == 0: return 
        
        def bfs(q):
            while q:
                i, j, d = q.popleft()
                for x, y in ((i+1, j),(i, j+1),(i-1, j),(i, j-1)):
                    if 0<=x<m and 0<=y<n:
                        if d+1<rooms[x][y]:
                            rooms[x][y] = d+1
                            q.append((x, y, d+1))

        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    q = deque()
                    q.append((i, j, 0))
                    bfs(q)

test = Solution()
testCase = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
    ]
test.wallsAndGates(testCase)
print testCase
