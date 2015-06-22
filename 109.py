# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {ListNode} head
	# @return {TreeNode}
	def sortedListToBST(self, head):
		if head == None:
			return None
		n = 0
		self.p = head
		while head != None:
			head = head.next
			n += 1
		return self.dfs(0, n)

	def dfs(self, start, end):
		if start >= end:
			return None
		# print start, end	
		m = (start + end) >> 1
		node = TreeNode(0)
		node.left = self.dfs(start, m)
		node.val = self.p.val
		self.p = self.p.next
		node.right = self.dfs(m+1, end)
		return node

test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
root = test.sortedListToBST(head)
print root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val
