# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        oddHead, oddTail = None, None
        evenHead, evenTail = None, None
        odd = 1
        while head != None:
            if odd:
                if not oddHead:
                    oddHead, oddTail = head, head
                    head = head.next
                    oddHead.next, oddTail.next = None, None
                else:
                    oddTail.next = head
                    head = head.next
                    oddTail = oddTail.next
                    oddTail.next = None
                odd = 0
            else:
                if not evenHead:
                    evenHead, evenTail = head, head
                    head = head.next
                    evenHead.next, evenHead.next = None, None
                else:
                    evenTail.next = head
                    head = head.next
                    evenTail = evenTail.next
                    evenTail.next = None
                odd = 1

        head = oddHead
        cur = oddHead
        oddHead = oddHead.next
        while oddHead:
            cur.next = oddHead
            oddHead = oddHead.next
            cur = cur.next
        while evenHead:
            cur.next = evenHead
            evenHead = evenHead.next
            cur = cur.next
        return head
                
def p(n):
    while n != None:
        print n.val
        n = n.next
    print '---'
test = Solution()
p(test.oddEvenList(None))
l1 = ListNode(1)
p(test.oddEvenList(l1))
l2 = ListNode(1)
l2.next = ListNode(2)
p(test.oddEvenList(l2))
l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(3)
p(test.oddEvenList(l3))
l4 = ListNode(1)
l4.next = ListNode(2)
l4.next.next = ListNode(3)
l4.next.next.next = ListNode(4)
p(test.oddEvenList(l4))
l5 = ListNode(1)
l5.next = ListNode(2)
l5.next.next = ListNode(3)
l5.next.next.next = ListNode(4)
l5.next.next.next.next = ListNode(5)
p(test.oddEvenList(l5))
