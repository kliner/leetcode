class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        n, m = 0, 0
        if len(matrix) == 0:
            return
        n = len(matrix)
        m = len(matrix[0])
        if len(matrix[0]) == 0:
            return
        self.data = [[0 for col in range(m)] for row in range(n)]
        self.data[0][0] = matrix[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    self.data[i][j] = matrix[i][j] + self.data[i][j-1]
                elif j == 0:
                    self.data[i][j] = matrix[i][j] + self.data[i-1][j]
                else:
                    self.data[i][j] = matrix[i][j] + self.data[i-1][j] + self.data[i][j-1] - self.data[i-1][j-1]
        self.n = n
        self.m = m
        #print self.data 

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.data[row2][col2]
        elif row1 == 0:
            return self.data[row2][col2] - self.data[row2][col1-1]
        elif col1 == 0:
            return self.data[row2][col2] - self.data[row1-1][col2]
        else:
            return self.data[row2][col2] + self.data[row1-1][col1-1] - self.data[row2][col1-1] - self.data[row1-1][col2]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
            ]
    test = NumMatrix(matrix)
    print test.sumRegion(2,1,4,3)
    print test.sumRegion(1,1,2,2)
    print test.sumRegion(1,2,2,4)
    print test.sumRegion(0,0,1,1)
    print test.sumRegion(0,1,1,1)
    print test.sumRegion(1,0,1,1)
    matrix = [[-1]]
    test = NumMatrix(matrix)
    print test.sumRegion(0,0,0,0)
    matrix = [[1],[-7]]
    test = NumMatrix(matrix)
    print test.sumRegion(1,0,1,0)
    print test.sumRegion(0,0,1,0)

