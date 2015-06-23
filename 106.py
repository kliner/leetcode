# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {integer[]} inorder
	# @param {integer[]} postorder
	# @return {TreeNode}
	def buildTree(self, inorder, postorder):
		if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
			return None
		# a = postorder[-1]
		# b = inorder.index(a)
		# node = TreeNode(a)
		# node.left = self.buildTree(inorder[:b], postorder[:b])
		# node.right = self.buildTree(inorder[b+1:], postorder[b:-1])
		self.inorder = inorder
		self.postorder = postorder
		return self.buildByOrder(0, len(inorder), 0, len(postorder))

	def buildByOrder(self, inStart, inEnd, postStart, postEnd):
		if inStart >= inEnd or postStart >= postEnd:
			return None
		a = self.postorder[postEnd - 1]
		b = self.inorder[inStart:inEnd].index(a)
		node = TreeNode(a)
		node.left = self.buildByOrder(inStart, inStart + b, postStart, postStart + b)
		node.right = self.buildByOrder(inStart + b + 1, inEnd, postStart + b, postEnd - 1)
		return node

test = Solution()
root = test.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])
print root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val
# 1,2,3,4,5,6,7

# 4,2,5,1,6,3,7
# 4,5,2,6,7,3,1