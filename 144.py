# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	def preorderTraversal(self, root):
		if root == None:
			return []
		stack = [root]
		ans = []
		while len(stack) != 0:
			node = stack.pop()
			ans.append(node.val)
			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)
		return ans

t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
test = Solution()
print test.preorderTraversal(t)