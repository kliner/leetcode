class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import copy

class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def levelOrder(self, root):
		if root == None:
			return []
		ans = []
		s = [root]
		while len(s) != 0:
			ts = []
			a = []
			for i in s:
				a.append(i.val)
				if i.left != None:
					ts.append(i.left)
				if i.right != None:
					ts.append(i.right)
			s = ts
			ans.append(copy.copy(a))
		return ans

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)
print test.levelOrder(t)