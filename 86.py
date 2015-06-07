class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} x
	# @return {ListNode}
	def partition(self, head, x):
		cur = head
		bigHead = ListNode(-1)
		bigCur = bigHead
		smallHead = ListNode(-1)
		smallCur = smallHead
		while cur != None:
			if cur.val >= x:
				bigCur.next = ListNode(cur.val)
				bigCur = bigCur.next
			else:
				smallCur.next = ListNode(cur.val)
				smallCur = smallCur.next
			cur = cur.next
		smallCur.next = bigHead.next
		return smallHead.next

l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
test = Solution()
cur = test.partition(l1, 3)
while cur != None:
	print cur.val
	cur = cur.next
