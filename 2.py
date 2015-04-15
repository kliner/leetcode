# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):

    	head = ListNode(0) 
    	curr = head
    	tail = head
    	b = 0
    	while l1 != None and l2 != None:
			curr = tail
		 	t = l1.val + l2.val + b
			if t >= 10:
				t = t - 10
				b = 1
			else:
				b = 0
			tail = ListNode(0)
			curr.val = t
			curr.next = tail
			l1 = l1.next
			l2 = l2.next

    	while l1 != None:
			curr = tail
			tail = ListNode(0)
			t = l1.val + b
			if t >= 10:
				t = t - 10
				b = 1
			else:
				b = 0
			curr.val = t
			curr.next = tail
			l1 = l1.next

    	while l2 != None:
			curr = tail
			tail = ListNode(0)
			t = l2.val + b
			if t >= 10:
				t = t - 10
				b = 1
			else:
				b = 0
			curr.val = t
			curr.next = tail
			l2 = l2.next
    	if b == 1:
    		curr.next.val = 1
    	else:
    		curr.next = None
    	return head

a = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
# l1.next.next = ListNode(3)
l2 = ListNode(1)
l2.next = ListNode(6)
l = a.addTwoNumbers(l1, l2)
print l.val, l.next.val, l.next.next.val