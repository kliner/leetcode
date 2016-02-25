class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        n = len(preorder)

        stk = []
        last = -1e100
        for i in xrange(n):
            if not stk or preorder[i] < stk[-1]:
                stk.append(preorder[i])
            else:
                while stk and preorder[i] > stk[-1]:
                    t = stk.pop()
                    #print t
                    if t < last: return False 
                    last = t
                stk.append(preorder[i])
        #print stk
        while stk:
            t = stk.pop()
            if t < last: return False 
            last = t

        return True


test = Solution()
print test.verifyPreorder([4,2,1,3,6,5,7])
print test.verifyPreorder([4,6,5,7])
print test.verifyPreorder([4,2,1,3])
print test.verifyPreorder([2,3,1]) == False
print test.verifyPreorder([8,6,1,4,10])
