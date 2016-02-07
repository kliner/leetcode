# dfs, O(n*m)
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0: return 0
        n = len(image[0])
        if n == 0: return 0

        marked = [[0] * n for i in xrange(m)]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        ans = [y, y, x, x]
        
        def dfs(i, j):
            marked[i][j] = 1
            ans[0] = min(ans[0], j)
            ans[1] = max(ans[1], j)
            ans[2] = min(i, ans[2])
            ans[3] = max(i, ans[3])

            for k in xrange(4):
                tx = i+dx[k]
                ty = j+dy[k]
                if tx >= 0 and tx < m and ty >= 0 and ty < n and not marked[tx][ty] and image[tx][ty] == '1':
                    dfs(tx, ty)
        
        dfs(x, y)
        return (ans[1]-ans[0]+1)*(ans[3]-ans[2]+1)
        
test = Solution()
testCase = [
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
        ]
print test.minArea(testCase, 0, 2);
print test.minArea(testCase, 1, 1);
print test.minArea(testCase, 2, 1);

