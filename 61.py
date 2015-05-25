# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} k
	# @return {ListNode}
	def rotateRight(self, head, k):
		if k == 0:
			return head
		if head == None:
			return head
		c = k
		cur = head
		new = None
		while cur.next != None:
			if c == 0:
				new = head
				c -= 1
			elif c > 0:
				c -= 1
			else:
				new = new.next
			cur = cur.next
		# print c
		if c == 0:
			new = cur
		elif c > 0:
			n = k - c + 1
			k = k % n
			c = k
			# print c, n, k
			cur = head
			while cur.next != None:
				if c == 0:
					new = head
					c -= 1
				elif c > 0:
					c -= 1
				else:
					new = new.next
				cur = cur.next
			if c == 0:
				new = cur
		cur.next = head
		new = new.next
		# print cur.val, head.val, new.val
		ans = new.next
		new.next = None
		return ans

a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
e = ListNode(5)
d.next = e
test = Solution()
ans = test.rotateRight(a, 2)
while ans != None:
	print ans.val
	ans = ans.next