# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		h1 = head
		h2 = head
		while h1 != None:
			h1 = h1.next
			if not h1:
				return False
			else:
				h1 = h1.next
			h2 = h2.next
			if h1 == h2:
				return True
		return False

test = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
print test.hasCycle(n)
n.next.next.next = n.next
print test.hasCycle(n)