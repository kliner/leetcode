# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        n, half = 0, 0
        while cur != None:
            cur = cur.next
            n += 1

        if n % 2 == 1:
            half = (n+1) >> 1
        else:
            half = n >> 1
            
        cur = head
        for i in xrange(half):
            cur = cur.next
        mid = cur
        midHead = None
        while cur != None:
            nxt = cur.next
            cur.next = midHead
            midHead = cur
            cur = nxt
        
        while midHead != None:
            if midHead.val != head.val:
                return False
            midHead = midHead.next
            head = head.next
                
        return True
                

if __name__ == '__main__':
    test = Solution()
    n = ListNode(1)
    print test.isPalindrome(n)
    n.next = ListNode(6)
    print test.isPalindrome(n)
    n.next.next = ListNode(1)
    print test.isPalindrome(n)

        

