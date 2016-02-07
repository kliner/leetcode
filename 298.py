class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def visit(root, i):
            if not root: return
            self.ans = max(self.ans, i)
            if root.left and root.left.val == root.val+1: visit(root.left, i+1)
            else: visit(root.left, 1)
            if root.right and root.right.val == root.val+1: visit(root.right, i+1)
            else: visit(root.right, 1)

        visit(root, 1)
        return self.ans

test = Solution()
print test.longestConsecutive(None)
root = TreeNode(1)
print test.longestConsecutive(root)
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print test.longestConsecutive(root)
root = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(1)
print test.longestConsecutive(root)
