class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        ans = self.visit(citations, 0, n, n)
        if ans:
            return ans
        else:
            return 0

    def visit(self, citations, lo, hi, n):
        #print lo, hi
        if lo >= hi:
            return lo
        h = (lo + hi)>>1
        if citations[n-1-h] < h:
            return self.visit(citations, lo, h, n)
        elif citations[n-1-h] == h:
            return h
        else:
            return self.visit(citations, h+1, hi, n)


if __name__ == '__main__':
    test = Solution()
    print test.hIndex([])
    print test.hIndex([0])
    print test.hIndex([1])
    print test.hIndex([5, 5, 6, 7, 8])
    print test.hIndex([0,0,0,1,1,1,2,2,2])
    print test.hIndex([0,0,0,1,1,1,3,3,3])
