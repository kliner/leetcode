class Solution(object):

    # using extra n space, O(n)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        a = [0 for i in xrange(n+1)]
        for i in xrange(n):
            if citations[i]>=n:
                a[n]+=1
            else:
                a[citations[i]]+=1
        s = 0
        for i in xrange(1,n+1):
            s += a[n+1-i]
            if s >= n+1-i:
                return n+1-i

        return 0

if __name__ == '__main__':
    test = Solution()
    print test.hIndex([])
    print test.hIndex([0])
    print test.hIndex([1])
    print test.hIndex([7, 8, 6, 5, 5])
    print test.hIndex([3, 0, 6, 1, 5])
    print test.hIndex([2, 0, 1, 1, 2])

