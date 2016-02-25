# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = root
        last = None
        while cur.val != p.val:
            if cur.val < p.val:
                cur = cur.right
            elif cur.val > p.val:
                last = cur
                cur = cur.left

        if not cur.right: return last
        cur = cur.right
        while cur.left:
            cur = cur.left
        return cur

# 1 2 3 4 5 6 7
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
test = Solution()
print test.inorderSuccessor(root, root.right).val == 7
print test.inorderSuccessor(root, root.left).val == 3
print test.inorderSuccessor(root, root.right.right) is None
print test.inorderSuccessor(root, root.left.right).val == 4
print test.inorderSuccessor(root, root).val == 5
print test.inorderSuccessor(root, root.right.left).val == 6

