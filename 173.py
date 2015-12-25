# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        x = root
        while x:
            self.s.append(x)
            x = x.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.s) != 0
        

    def next(self):
        """
        :rtype: int
        """
        x = self.s.pop()
        r = x.right
        while r:
            self.s.append(r)
            r = r.left
        return x.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)
    test = BSTIterator(root)
    while test.hasNext():
        print test.next()
