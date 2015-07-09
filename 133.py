# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if node == None:
			return None
		newNode = UndirectedGraphNode(node.label)
		cur = [(node, newNode)]
		visit = {}
		while len(cur) != 0:
			t = []
			for c, n in cur:
				for nb in c.neighbors:
					if nb.label not in visit:
						newN = UndirectedGraphNode(nb.label)
						visit[nb.label] = newN
						t.append((nb, newN))
						n.neighbors.append(newN)
					else:
						n.neighbors.append(visit[nb.label])
			cur = t

		return newNode

n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n0.neighbors = [n1,n2]
n1.neighbors = [n0,n2]
n2.neighbors = [n0,n1,n2]
test = Solution()
n0 = test.cloneGraph(n0)
for i in n0.neighbors:
	print i.label
for i in n0.neighbors[0].neighbors:
	print i.label
for i in n0.neighbors[1].neighbors:
	print i.label