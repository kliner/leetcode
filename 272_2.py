# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.small_k = []
        self.great_k = []

        def visitL(node):
            if len(self.small_k) == k or not node: return
            visitL(node.right)
            if len(self.small_k) < k: self.small_k += [node.val]
            visitL(node.left)

        def floorK(node):
            if not node: return
            if node.val <= target:
                floorK(node.right)
                if len(self.small_k) < k: self.small_k += [node.val]
                visitL(node.left)
                return
            return floorK(node.left)

        def visitR(node):
            if len(self.great_k) == k or not node: return
            visitR(node.left)
            if len(self.great_k) < k: self.great_k += [node.val]
            visitR(node.right)

        def ceilK(node):
            if not node: return
            if node.val >= target:
                ceilK(node.left)
                if len(self.great_k) < k: self.great_k += [node.val]
                visitR(node.right)
                return
            return ceilK(node.right)
        
        floorK(root)
        ceilK(root)

        ans = []
        i, j = 0, 0
        for t in xrange(k):
            if i == len(self.small_k): 
                ans += [self.great_k[j]]
                j += 1
            elif j == len(self.great_k):
                ans += [self.small_k[i]]
                i += 1
            elif self.small_k[i] == self.great_k[j]:
                ans += [self.small_k[i]]
                i += 1
                j += 1
            elif self.great_k[j] - target < target - self.small_k[i]:
                ans += [self.great_k[j]]
                j += 1
            else:
                ans += [self.small_k[i]]
                i += 1
        return ans

test = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print test.closestKValues(root, 4.0, 3)
print test.closestKValues(root, 3.9, 3)
print test.closestKValues(root, 4.1, 3)
print test.closestKValues(root, 5.1, 3)
print test.closestKValues(root, 6.1, 3)
print test.closestKValues(root, 9.1, 3)
print test.closestKValues(root, 0.1, 3)
