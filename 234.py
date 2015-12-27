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
        newHead = None
        while cur != None:
            tmp = ListNode(cur.val)
            tmp.next = newHead
            newHead = tmp
            cur = cur.next
        cur = head
        while cur != None:
            if cur.val != newHead.val:
                return False
            cur = cur.next
            newHead = newHead.next
        return True
                

if __name__ == '__main__':
    test = Solution()
    n = ListNode(1)
    print test.isPalindrome(n)
    n.next = ListNode(6)
    print test.isPalindrome(n)
    n.next.next = ListNode(1)
    print test.isPalindrome(n)

        
