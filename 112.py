# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {boolean}
	def hasPathSum(self, root, s):
		if root == None:
			return False
		if root.left == None and root.right == None:
			if s == root.val:
				return True
			else:
				return False
		return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)

test = Solution()
t = TreeNode(5)
t.left = TreeNode(4)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right = TreeNode(8)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.right = TreeNode(1)
print test.hasPathSum(t, 22)

t.val = 100
print test.hasPathSum(t, 22)