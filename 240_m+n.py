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

        i, j = 0, n-1
        while i < m and j >= 0: 
            c = cmp(target, matrix[i][j])
            if c == 0:
                return True
            elif c < 0:
                j-=1
            else:
                i+=1
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
            [2,2],
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
