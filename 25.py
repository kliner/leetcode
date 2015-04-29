# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverse(self, prev, head, k):
		curr = head
		for i in xrange(k):
			# print curr.val
			t = curr.next
			curr.next = prev.next
			prev.next = curr
			curr = t

	# @param {ListNode} head
	# @param {integer} k
	# @return {ListNode}
	def reverseKGroup(self, head, k):
		res = ListNode(-1)
		res.next = head
		prev = res
		curr = head
		i = 0
		while curr != None:
			if i == k - 1:
				t = prev.next
				prev.next = curr.next
				curr = curr.next
				self.reverse(prev, t, k)
				i = 0
				prev = t
			else:
				curr = curr.next
				i += 1
		return res.next

test = Solution()
l = None
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
head = test.reverseKGroup(l, 1)
while head != None:
	print head.val
	head = head.next