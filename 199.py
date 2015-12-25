# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans
        lay = [root]
        while len(lay) != 0:
            ans.append(lay[-1].val)
            newLay = []
            for node in lay:
                if node.left != None:
                    newLay.append(node.left) 
                if node.right != None:
                    newLay.append(node.right) 
            lay = newLay
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    test = Solution()
    print test.rightSideView(root)

    root.left.right.left = TreeNode(6)
    print test.rightSideView(root)

        
