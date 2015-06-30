# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def maxPathSum(self, root):
		self.ans = -9999999999999999999999L
		self.dfs(root)
		return self.ans
		
	def dfs(self, root):
		if root == None:
			return 0
		lval = self.dfs(root.left)
		rval = self.dfs(root.right)
		if lval < 0 and rval >= 0:
			self.ans = max(self.ans, rval + root.val)
		elif rval < 0 and lval >= 0:
			self.ans = max(self.ans, lval + root.val)
		elif lval < 0 and rval < 0:
			self.ans = max(self.ans, root.val)
		else:
			self.ans = max(self.ans, lval + rval + root.val)
		return max(lval + root.val, rval + root.val, root.val)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(100)
node.left.right = TreeNode(100)
test = Solution()
print test.maxPathSum(node)
node.left = TreeNode(-1)
node.right = None
print test.maxPathSum(node)
