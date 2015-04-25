# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} n
	# @return {ListNode}
	def removeNthFromEnd(self, head, n):
		res = head
		t = head
		while t.next != None:
			if n > 0:
				n -= 1
			else:
				res = res.next
			t = t.next
		if n == 1:
			return head.next
		else:
			res.next = res.next.next
		return head

test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
t = head
head = test.removeNthFromEnd(head, 5)
while head != None:
	print head.val
	head = head.next