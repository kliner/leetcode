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
        self.visit(root, p, q, 0, 0)
        return self.ans

    def visit(self, x, p, q, findp, findq):
        if not x or self.ans:
            return findp, findq
        findp1, findq1 = self.visit(x.left, p, q, findp, findq)
        findp2, findq2 = self.visit(x.right, p, q, findp, findq)
        #print x.val
        if x == p:
            findp = 1
        if x == q:
            findq = 1
        findp = findp | findp1 | findp2
        findq = findq | findq1 | findq2
        if findp and findq and not self.ans:
            self.ans = x
        return findp, findq
                

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
