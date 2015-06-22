# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def minDepth(self, root):
		if root == None:
			return 0
		ans = 0
		s = [root]
		while len(s) != 0:
			ss = []
			ans += 1
			for i in s:
				if i.left != None:
					ss.append(i.left)
				if i.right != None:
					ss.append(i.right)
				if i.right == None and i.left == None:
					return ans
			s = ss

test = Solution()
print test.minDepth(None) == 0
t = TreeNode(1)
print test.minDepth(t) == 1
t.left = TreeNode(2) 
print test.minDepth(t) == 2
t.right = TreeNode(3)
print test.minDepth(t) == 2
t.left.left = TreeNode(4) 
print test.minDepth(t) == 2
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
print test.minDepth(t) == 3
t.right.right = TreeNode(7)
print test.minDepth(t) == 3
t.right.right.right = TreeNode(8)
print test.minDepth(t) == 3