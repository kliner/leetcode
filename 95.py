# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {integer} n
	# @return {TreeNode[]}
	def generateTrees(self, n):
		if n == 0:
			return [None]
		return self.dfs(1, n)

	def dfs(self, l, r):
		sub = []
		if l > r:
			return [None]
		for i in range(l, r+1):
			left = self.dfs(l, i-1)
			right = self.dfs(i+1, r)
			for j in left:
				for k in right:
					root = TreeNode(i)
					root.left = j
					root.right = k
					sub.append(root)

		return sub

test = Solution()
print test.generateTrees(0)
print test.generateTrees(1)[0].val
print test.generateTrees(3)