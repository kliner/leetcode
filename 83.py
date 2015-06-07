class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def deleteDuplicates(self, head):
		cur = head
		while cur != None:
			if cur.next == None:
				return head
			if cur.val == cur.next.val:
				cur.next = cur.next.next
			else:
				cur = cur.next

		return head

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)
l4 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
head = l1
test = Solution()
head = test.deleteDuplicates(l1)
while head != None:
	print head.val
	head = head.next