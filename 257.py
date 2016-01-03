# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        self.visit(root, None)
        return self.ans
        
    def visit(self, x, path):
        if not x:
            return
        if not path:
            path = str(x.val)
        else:
            path += '->' + str(x.val)
        if x.left == None and x.right == None:
            self.ans.append(path)
            return
        self.visit(x.left, path)
        self.visit(x.right, path)

        
if __name__ == '__main__':
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    print test.binaryTreePaths(root)
