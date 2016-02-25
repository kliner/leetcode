class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])

        def checkCol(col):
            return any(image[i][col] == '1' for i in xrange(m))

        def checkRow(row):
            return '1' in image[row]

        def findLeft():
            lo, hi = 0, y
            while lo < hi:
                mid = (lo+hi)/2
                if checkCol(mid): hi = mid
                else: lo = mid + 1
            return hi

        def findRight():
            lo, hi = y, n
            while lo < hi:
                mid = (lo+hi)/2
                if checkCol(mid): lo = mid + 1
                else: hi = mid
            return hi

        def findTop():
            lo, hi = 0, x
            while lo < hi:
                mid = (lo+hi)/2
                if checkRow(mid): hi = mid
                else: lo = mid + 1
            return hi

        def findBottom():
            lo, hi = x, m
            while lo < hi:
                mid = (lo+hi)/2
                if checkRow(mid): lo = mid + 1
                else: hi = mid
            return hi
            
        #print findTop(), findBottom(), findLeft(), findRight()
        return (findBottom()-findTop())*(findRight()-findLeft())

test = Solution()
testCase = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
        ]
print test.minArea(testCase, 0, 0);
testCase = [
        ["0","0","0"],
        ["0","1","0"],
        ["0","0","0"]
        ]
print test.minArea(testCase, 1, 1);
testCase = [
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
        ]
print test.minArea(testCase, 0, 2);
print test.minArea(testCase, 1, 1);
print test.minArea(testCase, 2, 1);

testCase = [
        ["0","0","1","0"],
        ["0","1","1","1"],
        ["0","1","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
        ]
print test.minArea(testCase, 2, 2);
