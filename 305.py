class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        cnt = 0
        root = {}

        def findRoot(x):
            while x != root[x][0]:
                root[x][0] = root[root[x][0]][0]
                x = root[x][0]
            return x

        for i, j in positions:
            cnt += 1
            root[i*n+j] = [i*n+j, 1]
            for x, y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                if 0<=x<m and 0<=y<n and x*n+y in root:
                    other = findRoot(x*n+y)
                    this = findRoot(i*n+j)
                    if this != other:
                        if root[other][1] < root[this][1]:
                            root[other][0] = this
                            root[this][1] += root[other][1]
                        else:
                            root[this][0] = other
                            root[other][1] = root[this][1]
                        cnt -= 1
            ans += [cnt]
        return ans

test = Solution()
print test.numIslands2(3,3,[[0,0], [0,1], [1,2], [2,1]])
print test.numIslands2(3,3,[[0,0], [0,1], [1,2], [2,1], [1,1]])
print test.numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])
print test.numIslands2(3,6,[[2,2],[2,1],[1,3],[0,4]])

