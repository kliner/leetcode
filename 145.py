# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	def postorderTraversal(self, root):
		stack = [root]
		ans = []
		dct1 = []
		dct2 = []
		while len(stack) != 0:
			cur = stack[-1]
			if cur == None:
				stack.pop()
				continue
			if cur not in dct1:
				dct1.append(cur)
				stack.append(cur.left)
			elif cur not in dct2:
				dct2.append(cur)
				stack.append(cur.right)
			else:
				ans.append(cur.val)
				stack.pop()
		return ans

t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
test = Solution()
print test.postorderTraversal(t)