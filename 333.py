# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        def visit(node):
            if node.left and node.right:
                cnt_l, b_l, lo_l, hi_l = visit(node.left)
                cnt_r, b_r, lo_r, hi_r = visit(node.right)
                if b_l and b_r and hi_l < node.val < lo_r:
                    return cnt_l + cnt_r + 1, True, lo_l, hi_r
                else:
                    return max(cnt_l, cnt_r), False, -1, -1
            elif node.left:
                cnt_l, b_l, lo_l, hi_l = visit(node.left)
                if b_l and hi_l < node.val:
                    return cnt_l + 1, True, lo_l, node.val
                else:
                    return cnt_l, False, -1, -1
            elif node.right:
                cnt_r, b_r, lo_r, hi_r = visit(node.right)
                if b_r and node.val < lo_r:
                    return cnt_r + 1, True, node.val, hi_r
                else:
                    return cnt_r, False, -1, -1
            else:
                return 1, True, node.val, node.val

        return visit(root)[0]


test = Solution()
print test.largestBSTSubtree(None)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(18)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print test.largestBSTSubtree(root)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(18)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(6)
root.right.right.left.left = TreeNode(5)
root.right.right.right = TreeNode(8)
root.right.right.right.right = TreeNode(9)
print test.largestBSTSubtree(root)
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
print test.largestBSTSubtree(root)
