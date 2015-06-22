# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	ans = 0
	# @param {TreeNode} root
	# @return {integer}
	def maxDepth(self, root):
		if root == None:
			return 0
		self.dfs(root, 1)
		return self.ans

	def dfs(self, root, depth):
		if depth > self.ans:
			self.ans = depth
		if root.left != None:
			self.dfs(root.left, depth+1)
		if root.right != None:
			self.dfs(root.right, depth+1)

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.left.right = TreeNode(5)
print test.maxDepth(t)