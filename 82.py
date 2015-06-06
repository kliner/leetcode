class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def deleteDuplicates(self, head):
		if head == None:
			return head
		ans = ListNode(-1)
		prev = ans
		prev.next = head
		cur = head
		while cur != None:
			f = False
			while cur.next != None and cur.val == cur.next.val:
				cur = cur.next
				f = True
			if not f:
				prev.next = cur
				prev = cur
			else:
				prev.next = cur.next
			cur = cur.next
		return ans.next

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
head = l1
# while head != None:
# 	print head.val
# 	head = head.next

test = Solution()
head = test.deleteDuplicates(l1)
while head != None:
	print head.val
	head = head.next

