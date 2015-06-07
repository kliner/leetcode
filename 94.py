# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	def inorderTraversal(self, root):
		stack = []
		ans = []
		cur = root
		while cur != None or len(stack) != 0:
			if cur != None:
				stack.append(cur)
				cur = cur.left
			else:
				cur = stack.pop()
				ans.append(cur.val)
				cur = cur.right
		return ans

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
test = Solution()
print test.inorderTraversal(t1)