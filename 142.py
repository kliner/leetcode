# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		h1 = head
		h2 = head
		while h1 != None:
			if h1.next != None:
				h1 = h1.next.next
			else:
				return None
			h2 = h2.next
			if h1 == h2:
				break
		if h1 == None:
			return None
		h3 = head
		while h3 != h1:
			h3 = h3.next
			h1 = h1.next
		return h3

test = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
print test.detectCycle(n)
n.next.next.next = n.next
print test.detectCycle(n)