class Digraph(object):
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in xrange(n)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

class CycleDigraph(object):
    def __init__(self, G):
        n = G.n
        self.n = G.n
        self.onStack = [None for i in xrange(n)]
        self.marked = [None for i in xrange(n)]
        self.edgeTo = [None for i in xrange(n)]
        self.cycle = []
        self.G = G 
        for v in xrange(self.n):
            if self.cycle == []:
                self.dfs(self.G, v)

    def hasCycle(self):
        return self.cycle != [] 

    def dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle:
                return
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
        self.onStack[v] = False

class DepthFirstOrder(object):
    def __init__(self, G):
        n = G.n
        self.n = n
        self.marked = [None for i in xrange(n)]
        self.preorder = []
        self.postorder = []
        for v in xrange(n):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.marked[v] = True
        self.preorder.append(v)
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.postorder.append(v)

    def reversePost(self):
        return self.postorder[::-1]

class TopologicalOrder(object):
    def __init__(self, G):
        cycle = CycleDigraph(G)
        if cycle.hasCycle():
            self.order = []
            return 
        order = DepthFirstOrder(G)
        self.order = order.reversePost()

    def getOrder(self):
        return self.order

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        digraph = Digraph(numCourses)
        for p in prerequisites:
            w = p[0]
            for v in p[1:]:
                digraph.addEdge(v,w)
        order = TopologicalOrder(digraph)
        return order.getOrder()
        
if __name__ == '__main__':
    test = Solution()
    print test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])

