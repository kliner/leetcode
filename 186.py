class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        
        def exch(i, j):
            t = s[i]
            s[i] = s[j]
            s[j] = t

        def reverse(lo, hi):
            i = lo
            j = hi-1
            while i < j:
                exch(i, j)
                i+=1
                j-=1

        n = len(s)
        lo = 0
        hi = n-1
        while lo < hi:
            exch(lo, hi)
            lo += 1
            hi -= 1
        lo = 0
        while lo < n:
            hi = lo
            while hi < n and s[hi] != ' ': hi += 1 
            reverse(lo, hi)
            hi += 1
            lo = hi

test = Solution()
testCase = []
test.reverseWords(testCase)
print testCase
testCase = ['a']
test.reverseWords(testCase)
print testCase
testCase = ['a','b','c']
test.reverseWords(testCase)
print testCase
testCase = ['a','b','c',' ','d']
test.reverseWords(testCase)
print testCase
