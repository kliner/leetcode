# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = root
        ans = []
        n = self.getLeftHeight(cur)
        if n == 0:
            return 0
        base = 2 ** (n-1)
        while cur != None:
            lh = self.getLeftHeight(cur.left)
            rh = self.getLeftHeight(cur.right)
            if lh == rh:
                cur = cur.right
                ans.append(1)
            else:
                cur = cur.left
                ans.append(0)
        ans = ans[:-1]
        if not ans:
            return 1
        last = 0
        for i in ans:
            last *= 2 
            last += i
        return base + last
        

    def getLeftHeight(self, root):
        cur = root
        cnt = 0
        while cur:
            cur = cur.left
            cnt += 1
        return cnt
        
if __name__ == '__main__':
    test = Solution()
    root = None
    print test.countNodes(root)
    root = TreeNode(1)
    print test.countNodes(root)
    root.left = TreeNode(2)
    print test.countNodes(root)
    root.right = TreeNode(4)
    print test.countNodes(root)
    root.left.left = TreeNode(2)
    print test.countNodes(root)
    root.left.right = TreeNode(2)
    print test.countNodes(root)
