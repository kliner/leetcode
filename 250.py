# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def count(node):
            if not node: return 0, None
            if not node.left and not node.right: return 1, node.val
            if not node.left:
                r, val = count(node.right)
                if node.val == val:
                    return r + 1, val
                return r, None
            elif not node.right:
                l, val = count(node.left)
                if node.val == val:
                    return l + 1, val
                return l, None
            l, v1 = count(node.left)
            r, v2 = count(node.right)
            if node.val == v1 == v2:
                return l+r+1, node.val
            return l+r, None

        return count(root)[0]

test = Solution()
print test.countUnivalSubtrees(None)
        
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right = TreeNode(5)
root.right.right = TreeNode(5)
print test.countUnivalSubtrees(root)
