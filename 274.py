class Solution(object):

    # sort, O(nlogn)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        print citations
        for i in xrange(n):
            if citations[i]>=n-i:
                return n-i
        return 0

if __name__ == '__main__':
    test = Solution()
    print test.hIndex([])
    print test.hIndex([7, 8, 6, 5, 5])
    print test.hIndex([3, 0, 6, 1, 5])
    print test.hIndex([2, 0, 1, 1, 2])
