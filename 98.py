# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isValidBST(self, root):
		if root == None:
			return True
		return self.dfs(root, -999999999999999L, 9999999999999L)

	def dfs(self, root, l, r):
		# print l, r
		if root.val <= l or root.val >= r:
			return False
		ans = True
		if root.left != None:
			# print 'left', root.left.val
			if root.left.val < r and root.left.val > l:
				ans = self.dfs(root.left, l, root.val)
			else:
				return False
		if not ans:
			return False
		if root.right != None:
			# print 'right', root.right.val
			if root.right.val > l and root.right.val < r:
				ans = self.dfs(root.right, root.val, r)
			else:
				return False
		return ans

t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.left.right = TreeNode(2)
test = Solution()
print test.isValidBST(t1) == True
t1.right.left = TreeNode(5)
print test.isValidBST(t1) == False
t1.right.left = TreeNode(2)
print test.isValidBST(t1) == False
print test.isValidBST(None) == True
