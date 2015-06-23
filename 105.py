class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {integer[]} preorder
	# @param {integer[]} inorder
	# @return {TreeNode}
	def buildTree(self, preorder, inorder):
		if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
			return None
		
		self.preorder = preorder
		self.inorder = inorder
		# a = preorder[0]
		# b = inorder.index(a)
		# node = TreeNode(a)
		# node.left = self.buildTree(preorder[1:1+b], inorder[:b])
		# node.right = self.buildTree(preorder[1+b:], inorder[1+b:])
		return self.buildByOrder(0, len(preorder), 0, len(inorder))

	def buildByOrder(self, preStart, preEnd, inStart, inEnd):
		if preStart >= preEnd or inStart >= inEnd:
			return None
		a = self.preorder[preStart]
		b = self.inorder[inStart:inEnd].index(a)

		node = TreeNode(a)
		node.left = self.buildByOrder(preStart + 1, preStart + 1 + b, inStart, inStart + b)
		node.right = self.buildByOrder(preStart + 1 + b, preEnd, inStart + 1 + b, inEnd)
		return node


test = Solution()
root = test.buildTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
print root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val
# 1,2,3,4,5,6,7

# 1,2,4,5,3,6,7
# 4,2,5,1,6,3,7