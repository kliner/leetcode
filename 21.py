# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} l1
	# @param {ListNode} l2
	# @return {ListNode}
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		elif l2 == None:
			return l1
		if l1.val < l2.val:
			res = l1
			cur = l1
			l1 = l1.next
		else:
			res = l2
			cur = l2
			l2 = l2.next

		while l1 != None and l2 != None:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
				cur = cur.next
			else:
				cur.next = l2
				l2 = l2.next
				cur = cur.next

		if l1 == None:
			cur.next = l2
		elif l2 == None:
			cur.next = l1
		return res

test = Solution()
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(5)
l2.next.next = ListNode(6)
l = test.mergeTwoLists(l1, l2)
while l != None:
	print l.val
	l = l.next


