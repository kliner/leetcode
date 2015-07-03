class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def sumNumbers(self, root):
		self.ans = 0
		if root == None:
			return 0
		self.dfs(root, 0)
		return self.ans
		
	def dfs(self, root, val):
		if root.left == None and root.right == None:
			self.ans += (val * 10 + root.val)
			return
		if root.left != None:
			self.dfs(root.left, val * 10 + root.val)
		if root.right != None:
			self.dfs(root.right, val * 10 + root.val)


test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print test.sumNumbers(root)