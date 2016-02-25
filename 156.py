# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        ans = root
        while ans and ans.left:
            ans = ans.left

        def rotate(node):
            if not node: return
            l = rotate(node.left)
            if l:
                l.right = node
                l.left = rotate(node.right)
                node.left = node.right = None
            return node

        rotate(root)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
test = Solution()
r = test.upsideDownBinaryTree(root)
print r.val, r.left.val, r.right.val, r.right.left.val, r.right.right.val
