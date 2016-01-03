class Graph(object):
    def __init__(self, n):
        self.n = n
        self.adj = [set([]) for i in xrange(n)]
        self.height = [1e10 for i in xrange(n)]

    def addEdge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    def getLeafs(self):
        return [v for v in xrange(self.n) if len(self.adj[v]) == 1]

    def getMinHeight(self):
        if self.n == 1:
            return [0]
        leafs = self.getLeafs()
        cnt = self.n
        while cnt > 2:
            newLeafs = []
            cnt -= len(leafs)
            for v in leafs:
                w = self.adj[v].pop()
                self.adj[w].remove(v)
                if len(self.adj[w]) == 1:
                    newLeafs.append(w)
            leafs = newLeafs

        return leafs

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        G = Graph(n)
        for e in edges:
            G.addEdge(e[0], e[1])

        return G.getMinHeight()
        
        
if __name__ == '__main__':
    test = Solution()
    print test.findMinHeightTrees(1, [])
    print test.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    print test.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    print test.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
    print test.findMinHeightTrees(8, [[0,1],[1,2],[2,3],[3,4],[1,5],[2,6],[3,7]])

