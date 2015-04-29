# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def swapPairs(self, head):
		if head == None or head.next == None:
			return head
		
		t = None
		curr = head
		res = ListNode(-1)
		prev = res
		while curr != None:
			if t == None:
				t = curr
				curr = curr.next
				continue
			prev.next = curr
			t.next = curr.next
			curr.next = t
			prev = t
			curr = prev.next
			t = None

		return res.next


test = Solution()
l = None
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
head = test.swapPairs(l)
while head != None:
	print head.val
	head = head.next
