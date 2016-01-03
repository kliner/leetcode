# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recusive version, the left side of node will be visited many times.
class Solution(object):

    def visit(self, x):
        if not x:
            return 0
        return self.visit(x.left) + self.visit(x.right) + 1

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root:
            left = self.visit(root.left)
        else:
            return 0

        if left == k-1:
            return root.val
        elif left > k-1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left-1)


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
