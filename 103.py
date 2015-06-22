# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import copy
class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def zigzagLevelOrder(self, root):
		if root == None:
			return []
		ans = []
		s = [root]
		direct = 'r'
		while len(s) != 0:
			ss = []
			a = []
			for i in s:
				a.append(i.val)
				if direct == 'r':
					if i.left != None:
						ss.append(i.left)
					if i.right != None:
						ss.append(i.right)
				else:	
					if i.right != None:
						ss.append(i.right)
					if i.left != None:
						ss.append(i.left)
			if direct == 'r':
				direct = 'l'
			else:
				direct = 'r'
			ans.append(copy.copy(a))
			s = ss[::-1]
		return ans

test = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)
print test.zigzagLevelOrder(t)
t.left.left = TreeNode(4)
t.right.left = None
print test.zigzagLevelOrder(t)
