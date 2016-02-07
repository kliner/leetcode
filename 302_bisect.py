# bisect, O(nLog(m)+mLog(n))
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0: return 0
        n = len(image[0])
        if n == 0: return 0

        def findTop(lo, hi):
            while lo < hi:
                m = (lo+hi)>>1
                if '1' in image[m]: hi = m
                else: lo = m + 1
            return lo

        def findBottom(lo, hi):
            while lo < hi:
                m = (lo+hi)>>1
                if '1' in image[m]: lo = m + 1
                else: hi = m
            return lo 

        def findLeft(lo, hi, M):
            while lo < hi:
                m = (lo+hi)>>1
                if any(image[x][m]=='1' for x in xrange(M)): hi = m
                else: lo = m + 1
            return lo

        def findRight(lo, hi, M):
            while lo < hi:
                m = (lo+hi)>>1
                if all(image[x][m]=='0' for x in xrange(M)): hi = m
                else: lo = m + 1
            return lo
        
        return (findRight(y+1, n, m)-findLeft(0, y, m))*(findBottom(x+1, m)-findTop(0, x))
        
test = Solution()
testCase = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
        ]
print test.minArea(testCase, 0, 0);
testCase = [
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
        ]
print test.minArea(testCase, 0, 2);
print test.minArea(testCase, 1, 1);
print test.minArea(testCase, 2, 1);

