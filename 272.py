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
        self.k = k

        def dfsRight(root, lst):
            if not root: return
            dfsRight(root.right, lst)
            if len(lst) < self.k:
                lst.append(root.val)
            if len(lst) < self.k:
                dfsRight(root.left, lst)

        def dfsLeft(root, lst):
            if not root: return
            dfsLeft(root.left, lst)
            if len(lst) < self.k:
                lst.append(root.val)
            if len(lst) < self.k:
                dfsLeft(root.right, lst)

        def floor(root, target):
            if not root: return
            if root.val > target: 
                return floor(root.left, target)
            
            if root.val == target: 
                r = [root.val]
            else:
                r = floor(root.right, target)
            if r:
                if len(r) < self.k:
                    if r[0] != root.val:
                        r.append(root.val)
                    dfsRight(root.left, r)
                return r
            r = [root.val]
            dfsRight(root.left, r)
            return r

        def ceil(root, target):
            if not root: return
            if root.val < target:
                return ceil(root.right, target)

            if root.val == target: 
                l = [root.val]
            else:
                l = ceil(root.left, target)
            if l:
                if len(l) < self.k:
                    if l[0] != root.val:
                        l.append(root.val)
                    dfsLeft(root.right, l)
                return l
            l = [root.val]
            dfsLeft(root.right, l)
            return l

        lo = floor(root, target)
        #print lo
        hi = ceil(root, target)
        #print hi

        ans = []
        i, j = 0, 0
        for t in xrange(k):
            if not lo or i == len(lo):
                ans.append(hi[j])
                j += 1
            elif not hi or j == len(hi):
                ans.append(lo[i])
                i += 1
            elif lo[i] == hi[j]:
                ans.append(lo[i])
                i += 1
                j += 1
            elif target - lo[i] < hi[j] - target:
                ans.append(lo[i])
                i += 1
            else:
                ans.append(hi[j])
                j += 1
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
