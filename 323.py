class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        a = [0] * n
        sz = [1] * n
        for i in xrange(n):
            a[i] = i
        
        def root(i):
            while a[i] != i:
                a[i] = a[a[i]]
                i = a[i]
            return i
        
        def union(i, j):
            i = root(i)
            j = root(j)
            if i == j:
                return
            if sz[i] < sz[j]:
                a[i] = j
                sz[j] += sz[i]
            else:
                a[j] = i
                sz[i] += sz[j]
        
        for x, y in edges:
            union(x, y)

        ans = set([])
        for i in xrange(n):
            ans.add(root(i))
        return len(ans)

test = Solution()
print test.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
print test.countComponents(5, [[0, 1], [1, 2], [3, 4]])

