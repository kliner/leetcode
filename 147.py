# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def insertionSortList(self, head):
		if head == None or head.next == None:
			return head
		newHead = ListNode(0)
		newHead.next = head
		cur = head
		while cur.next != None:
			if cur.next.val >= cur.val:
				cur = cur.next
			else:
				pre = newHead
				while pre.next.val < cur.next.val:
					pre = pre.next
				t = cur.next
				cur.next = t.next
				t.next = pre.next
				pre.next = t

		return newHead.next

n = ListNode(3)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(5)
n.next.next.next.next = ListNode(4)
test = Solution()
t = test.insertionSortList(n)
while t != None:
	print t.val
	t = t.next
n = ListNode(3)
n.next = ListNode(4)
n.next.next = ListNode(2)
t = test.insertionSortList(n)
while t != None:
	print t.val
	t = t.next