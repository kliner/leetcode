class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		if head == None:
			return None
		newHead = RandomListNode(head.label)
		d = {head.label:newHead}
		q = [(head, newHead)]
		while len(q) != 0:
			old, new = q.pop()
			if old.next != None:
				if old.next.label not in d:
					t = RandomListNode(old.next.label)
					d[old.next.label] = t
					new.next = t
					q.append((old.next, new.next))
				else:
					new.next = d[old.next.label]
			if old.random != None:
				if old.random.label not in d:
					t = RandomListNode(old.random.label)
					d[old.random.label] = t
					new.random = t
					q.append((old.random, new.random))
				else:
					new.random = d[old.random.label]
		return newHead

test = Solution()
n = RandomListNode(1)
n.next = RandomListNode(2)
n.next.next = RandomListNode(3)
n.next.random = n.next.next
n.next.next.random = n
t = test.copyRandomList(n)
print n.label
print n.next.label
print n.next.next.label
print n.next.random.label
print n.next.next.random.label