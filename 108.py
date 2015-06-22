# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {integer[]} nums
	# @return {TreeNode}
	def sortedArrayToBST(self, nums):
		if len(nums) == 0:
			return None
		m = len(nums) >> 1
		node = TreeNode(nums[m])
		node.left = self.sortedArrayToBST(nums[:m])
		node.right = self.sortedArrayToBST(nums[m+1:])
		return node

test = Solution()
root = test.sortedArrayToBST([1,2,3,4,5,6,7])
print root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val
