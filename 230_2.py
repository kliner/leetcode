# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# inorder travesal, O(n)
class Solution(object):

    def visit(self, x, k):
        if not x or self.ans:
            return
        self.visit(x.left, k)
        self.idx += 1
        if self.idx == k:
            self.ans = x.val
            return
        self.visit(x.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans = None
        self.idx = 0
        self.visit(root, k)
        return self.ans


if __name__ == '__main__':
    test = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    print test.kthSmallest(root, 4)
    root = TreeNode(1)
    root.right = TreeNode(5)
    print test.kthSmallest(root, 2)
