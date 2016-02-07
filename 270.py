# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        def floor(root, target):
            if not root: return 
            if root.val == target: return root
            if root.val > target: return floor(root.left, target)
            r = floor(root.right, target)
            if r: return r
            else: return root
        
        def ceil(root, target):
            if not root: return
            if root.val == target: return root
            if root.val < target: return ceil(root.right, target)
            l = ceil(root.left, target)
            if l: return l
            else: return root

        l = floor(root, target)
        r = ceil(root, target)
        if not l: return r.val
        if not r: return l.val
        if target-l.val < r.val-target: return l.val
        else: return r.val

test = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print test.closestValue(root, 3.9) == 4
print test.closestValue(root, 5.1) == 5
print test.closestValue(root, 0.1) == 1
print test.closestValue(root, 9.9) == 7
