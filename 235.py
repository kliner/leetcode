# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.visit(root, p, q)
        return self.ans

    def visit(self, x, p, q):
        if not x or self.ans:
            return 
        if x.val == p.val or x.val == q.val:
            if self.inTree(x, q) and self.inTree(x, p):
                self.ans = x
                return 
        if self.inTree(x.left, p) and self.inTree(x.left, q):
            self.visit(x.left, p, q)
        elif self.inTree(x.right, p) and self.inTree(x.right, q):
            self.visit(x.right, p, q)
        elif self.inTree(x.left, p) and self.inTree(x.right, q):
            self.ans = x
        elif self.inTree(x.right, p) and self.inTree(x.left, q):
            self.ans = x

    def inTree(self, x, v):
        if not x:
            return False
        if x.val == v.val:
            return True
        if v.val < x.val:
            return self.inTree(x.left, v) 
        if v.val > x.val:
            return self.inTree(x.right, v)
        
if __name__ == '__main__':
    test = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print test.lowestCommonAncestor(root, root.left, root.right).val
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    print test.lowestCommonAncestor(root, root.right, root.left).val
