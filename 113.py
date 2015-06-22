# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import copy
class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {integer[][]}
	def pathSum(self, root, s):
		if root == None:
			return []
		self.ans = []
		self.dfs(root, s, [])
		return self.ans

	def dfs(self, root, s, a):
		if root == None:
			return
		if root.left == None and root.right == None:
			if s == root.val:
				a.append(s)
				self.ans.append(copy.copy(a))
				a.pop()
			return
		a.append(root.val)
		self.dfs(root.left, s - root.val, a)
		self.dfs(root.right, s - root.val, a)
		a.pop()

test = Solution()
t = TreeNode(5)
t.left = TreeNode(4)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right = TreeNode(8)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.left = TreeNode(5)
print test.pathSum(t, 22)