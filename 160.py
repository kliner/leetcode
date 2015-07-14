# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		n1 = 0	
		t = headA
		while t != None:
			t = t.next
			n1 += 1
		n2 = 0
		t = headB
		while t != None:
			t = t.next
			n2 += 1
		if n1 > n2:
			t1 = headA
			for i in xrange(n1 - n2):
				t1 = t1.next
			t2 = headB
		else:
			t2 = headB
			for i in xrange(n2 - n1):
				t2 = t2.next
			t1 = headA
		while t1 != None:
			if t1 == t2:
				return t1
			else:
				t1 = t1.next
				t2 = t2.next
		return None

test = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h2 = ListNode(3)
h3 = ListNode(4)
h1.next.next = h3
h2.next = h3
print test.getIntersectionNode(h1, h2).val