class Digraph(object):
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in xrange(n)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

class CycleDigraph(object):
    def __init__(self, digraph):
        n = digraph.n
        self.n = digraph.n
        self.onStack = [None for i in xrange(n)]
        self.marked = [None for i in xrange(n)]
        self.edgeTo = [None for i in xrange(n)]
        self.cycle = []
        self.digraph = digraph

    def checkCycle(self):
        for v in xrange(self.n):
            if self.cycle == []:
                self.dfs(self.digraph, v)
            else:
                return False
        return True

    def dfs(self, digraph, v):
        self.onStack[v] = True
        self.marked[v] = True
        for w in digraph.adj[v]:
            if self.cycle:
                return
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(digraph, w)
            elif self.onStack[w]:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
        self.onStack[v] = False

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        digraph = Digraph(numCourses)
        for p in prerequisites:
            w = p[0]
            for v in p[1:]:
                digraph.addEdge(v,w)
        
        cycle = CycleDigraph(digraph)
        return cycle.checkCycle()
        
        
if __name__ == '__main__':
    test = Solution()
    print test.canFinish(2, [[1,0],[0,1]])
    print test.canFinish(2, [[1,0]])
    print test.canFinish(2, [[0,1]])
