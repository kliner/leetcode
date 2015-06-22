# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isBalanced(self, root):
		if self.balanceHeight(root) >= 0:
			return True
		else:
			return False

	def balanceHeight(self, root):
		if root == None:
			return 0
		else:
			l = self.balanceHeight(root.left)
			r = self.balanceHeight(root.right)
			if l == -1 or r == -1:
				return -1
			if l == r + 1 or r == l + 1 or r == l:
				return max(l, r) + 1
			else:
				return -1

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
print test.isBalanced(t)
t.left.left.right = TreeNode(5)
print test.isBalanced(t)