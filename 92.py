# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} m
	# @param {integer} n
	# @return {ListNode}
	def reverseBetween(self, head, m, n):
		if m == n:
			return head
		cur = ListNode(-1)
		prev = cur
		cur.next = head
		for i in range(m-1):
			cur = cur.next
		oldTail = cur
		cur = cur.next
		newTail = cur
		newCur = cur
		cur = cur.next
		for i in range(n-m-1):
			t = cur.next
			cur.next = newCur
			newCur = cur
			cur = t
		newTail.next = cur.next
		newHead = cur
		cur.next = newCur
		oldTail.next = newHead
		if prev == oldTail:
			return newHead
		else:
			return head

if __name__ == '__main__':
	l1 = ListNode(1)
	l2 = ListNode(2)
	l3 = ListNode(3)
	l4 = ListNode(4)
	l5 = ListNode(5)
	l1.next = l2
	l2.next = l3
	l3.next = l4
	l4.next = l5
	test = Solution()
	cur = test.reverseBetween(l1, 1, 2)
	while cur != None:
		print cur.val
		cur = cur.next