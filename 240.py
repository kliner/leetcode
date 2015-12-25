class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False 

        return self.fourWaySearch(matrix, 0, m-1, 0, n-1, target)
        
    def fourWaySearch(self, matrix, xlo, xhi, ylo, yhi, target):
        #print xlo, xhi, ylo, yhi
        xm = (xlo + xhi) >> 1
        ym = (ylo + yhi) >> 1
        if xlo == xhi and ylo == yhi:
            return matrix[xlo][ylo] == target
        if xlo == xhi and ylo+1 == yhi:
            return matrix[xlo][ylo] == target or matrix[xhi][yhi] == target
        if xlo+1 == xhi and ylo == yhi:
            return matrix[xlo][ylo] == target or matrix[xhi][yhi] == target
        if xlo+1 == xhi and ylo+1 == yhi:
            return matrix[xlo][ylo] == target or matrix[xhi][yhi] == target or matrix[xlo][yhi] == target or matrix[xhi][ylo] == target

        
        if xlo > xhi or ylo > yhi:
            return False
        
        if target == matrix[xm][ym]:
            return True

        lo = matrix[xlo][ylo]
        hi = matrix[xm][ym]
        if target == lo or target == hi:
            return True
        if target > lo and target < hi:
            if self.fourWaySearch(matrix, xlo, xm, ylo, ym, target):
                return True
        lo = matrix[xm][ylo] 
        hi = matrix[xhi][ym]
        if target == lo or target == hi:
            return True
        if target > lo and target < hi:
            if self.fourWaySearch(matrix, xm, xhi, ylo, ym, target):
                return True
        lo = matrix[xlo][ym] 
        hi = matrix[xm][yhi]
        if target == lo or target == hi:
            return True
        if target > lo and target < hi:
            if self.fourWaySearch(matrix, xlo, xm, ym, yhi, target):
                return True
        lo = matrix[xm][ym] 
        hi = matrix[xhi][yhi]
        if target == lo or target == hi:
            return True
        if target > lo and target < hi:
            if self.fourWaySearch(matrix, xm, xhi, ym, yhi, target):
                return True
            
        return False


if __name__ == '__main__':
    test = Solution()
    matrix = [
            [0,1],
            [2,3]
            ]
    print test.searchMatrix(matrix, 1)

    matrix = [
            [1,3,5],
            ]
    print test.searchMatrix(matrix, 1)

    matrix = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
            ]

    print test.searchMatrix(matrix, 5)
    print test.searchMatrix(matrix, 20)
