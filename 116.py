# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
		t = TreeLinkNode(-1)
		p = t
		while root != None:
			if root.left != None:
				t.next = root.left
				t = t.next
			if root.right != None:
				t.next = root.right
				t = t.next
			root = root.next
		self.connect(p.next)

t = TreeLinkNode(1)
t.left = TreeLinkNode(2)
t.right = TreeLinkNode(3)
t.left.left = TreeLinkNode(4)
t.left.right = TreeLinkNode(5)
t.right.right = TreeLinkNode(6)
test = Solution()
test.connect(t)
print t.left.next.val
print t.left.left.next.val
print t.left.left.next.next.val
print t.left.left.next.next.next