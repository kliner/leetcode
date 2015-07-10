# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {void} Do not return anything, modify head in-place instead.
	def reorderList(self, head):
		if head == None:
			return
		h1 = head
		h2 = head
		while True:
			if h1.next == None or h1.next.next == None:
				t = h2
				h2 = h2.next
				t.next = None
				break
			else:
				h1 = h1.next.next
				h2 = h2.next
		
		head1 = head
		head2 = h2
		if head2 == None:
			return
		cur = head2.next
		head2.next = None
		while cur != None:
			t = cur.next
			cur.next = head2
			head2 = cur
			cur = t

		# h1 = head1
		# while h1 != None:
		# 	print h1.val
		# 	h1 = h1.next
		# h1 = head2
		# while h1 != None:
		# 	print h1.val
		# 	h1 = h1.next

		while head1 != None and head2 != None:
			t1 = head1.next
			t2 = head2.next
			head1.next = head2
			head2.next = t1
			head1 = t1
			head2 = t2

test = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
test.reorderList(h)
while h != None:
	print h.val
	h = h.next