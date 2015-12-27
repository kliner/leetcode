# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        newHead = None
        while cur:
            nxt = cur.next
            cur.next = newHead
            newHead = cur
            cur = nxt
        return newHead
            
        
if __name__ == '__main__':
    test = Solution()
