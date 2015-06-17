# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		if (p == None and q != None) or (p != None and q == None):
			return False
		if p == None and q == None:
			return True
		if p.val == q.val:
			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
		else:
			return False

test = Solution()
t1 = TreeNode(5)
t2 = TreeNode(5)
t1.left = TreeNode(1)
t2.left = TreeNode(1)
t1.left.right = TreeNode(2)
t2.left.right = TreeNode(2)
print test.isSameTree(t1, t2)
print test.isSameTree(None, t1)
print test.isSameTree(None, None)
t1.left.val = 123
print test.isSameTree(t1, t2)