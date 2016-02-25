# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dct = {}
        if root is None: return []
        q = deque()
        q.append((root, 0))
        while q:
            node, idx = q.popleft()
            if idx in dct:
                dct[idx].append(node.val)
            else:
                dct[idx] = [node.val]

            if node.left: q.append((node.left, idx-1))
            if node.right: q.append((node.right, idx+1))

        keys = dct.keys()
        keys.sort()
        ans = [dct[k] for k in keys]
        return ans


test = Solution()
print test.verticalOrder(None)
# 1 2 3 4 5 6 7
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print test.verticalOrder(root)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(2)
root.left.right.right = TreeNode(4)
print test.verticalOrder(root)
