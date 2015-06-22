# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import copy
class Solution:
	ans = []
	# @param {TreeNode} root
	# @return {integer[][]}
	def levelOrderBottom(self, root):
		if root == None:
			return []
		self.ans = []
		s = [root]
		while len(s) != 0:
			ss = []
			a = []
			for n in s:
				a.append(n.val)
				if n.left != None:
					ss.append(n.left)
				if n.right != None:
					ss.append(n.right)
			s = ss
			self.ans.append(copy.copy(a))
		return self.ans[::-1]

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
# t.right = TreeNode(3)
# t.right.left = TreeNode(4)
# t.right.right = TreeNode(5)
print test.levelOrderBottom(t)