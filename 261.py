class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj = [ [] for _ in xrange(n) ]
        if len(edges) < n-1: return False
        for v, w in edges:
            adj[v].append(w)
            adj[w].append(v)
        marked = [0] * n

        def dfs(v, last):
            marked[v] = 1
            for w in adj[v]:
                if w != last:
                    if not marked[w]: 
                        if not dfs(w, v): return False
                    else: return False
            return True

        if not dfs(0, -1): return False
        #print marked
        for i in xrange(n):
            if not marked[i]:
                return False
        return True

test = Solution()
print test.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]])
print test.validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
print test.validTree(5,[[0, 1], [1, 2], [3, 4]])
print test.validTree(5,[[0, 1], [3, 2], [2, 4], [3, 4]])
