# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

from Queue import PriorityQueue
class Solution:
	# @param {ListNode[]} lists
	# @return {ListNode}
	def mergeKLists(self, lists):
		n = len(lists)
		pq = PriorityQueue()
		for i in xrange(n):
			if lists[i] != None:
				pq.put( (lists[i].val, i) )
				lists[i] = lists[i].next
		curr = ListNode(-1)
		head = curr
		
		while pq.qsize() > 0:
			[val, i] = pq.get()
			t = ListNode(val)
			curr.next = t
			curr = t
			if lists[i] != None:
				pq.put( (lists[i].val, i) )
				lists[i] = lists[i].next

		return head.next

test = Solution()
ll = []
l1 = ListNode(1)
l1.next = ListNode(4)
l2 = ListNode(3)
l2.next = ListNode(7)
l3 = ListNode(2)
l3.next = ListNode(5)
l3.next.next = ListNode(6)
l4 = None
ll.append(l1)
ll.append(l2)
ll.append(l3)
ll.append(l4)
head = test.mergeKLists(ll)
while head != None:
	print head.val
	head = head.next
