# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        cur = head
        while cur and cur.val is val:
            cur = cur.next
        start = cur
        if not cur:
            return None
        while cur.next != None:
            if cur.next.val is val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return start


if __name__ == '__main__':
    test = Solution()
    n = ListNode(6)
    n.next = ListNode(1)
    s = test.removeElements(n, 6)
    print s
    print s.val
    print s.next
