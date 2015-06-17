# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isSymmetric(self, root):
		if root == None or (root.left == None and root.right == None):
			return True
		if (root.left == None and root.right != None) or (root.left != None and root.right == None):
			return False
		return self.judge(root.left, root.right)

	def judge(self, l, r):
		if (l == None and r == None):
			return True
		if (l == None and r != None) or (r == None and l != None):
			return False
		if l.val != r.val:
			return False
		return self.judge(l.left, r.right) and self.judge(l.right, r.left)

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.right.right = TreeNode(3)
print test.isSymmetric(t)
t.right.left = TreeNode(3)
print test.isSymmetric(t)