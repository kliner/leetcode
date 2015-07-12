# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def sortList(self, head):
		if head == None or head.next == None:
			return head

		h1 = head
		h2 = self.split(head)
		# if h2 != None:
		# 	print h2.val
		h1 = self.sortList(h1)
		h2 = self.sortList(h2)

		return self.merge(h1, h2)
		

	def split(self, head):
		if head == None:
			return None
		p1 = head
		p2 = head
		while p1.next != None:
			p1 = p1.next
			if p1.next != None:
				p1 = p1.next
				p2 = p2.next
		t = p2.next
		p2.next = None
		return t

	def merge(self, h1, h2):
		if h1 == None:
			return h2
		if h2 == None:
			return h1

		res = ListNode(0)
		cur = res
		while h1 != None or h2 != None:
			if h1 == None:
				cur.next = h2
				break
			if h2 == None:
				cur.next = h1
				break
			if h1.val < h2.val:
				cur.next = h1
				cur = cur.next
				h1 = h1.next
			else:
				cur.next = h2
				cur = cur.next
				h2 = h2.next
		return res.next

n = ListNode(3)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(5)
n.next.next.next.next = ListNode(4)
test = Solution()
a = test.sortList(n)
while a != None:
	print a.val
	a = a.next

n = ListNode(0)
t = n
for i in range(1, 10000):
	n.next = ListNode(i)
	n = n.next
a = test.sortList(t)
