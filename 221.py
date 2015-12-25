class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None:
            return 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        a = [[0 for col in range(n)] for row in range(m)]

        for i in xrange(m):
            for j in xrange(n):
                if i == '0' or j == '0':
                    if matrix[i][j] == '1':
                        a[i][j] = 1
                elif matrix[i][j] == '1':
                    a[i][j] = min(a[i-1][j], a[i-1][j-1], a[i][j-1]) + 1

        d = max([max(t) for t in a])
        return d ** 2
        


if __name__ == '__main__':
    test = Solution()
    matrix = []
    print test.maximalSquare(matrix) # = 0

    matrix = [[1]]
    print test.maximalSquare(matrix) # = 1

    matrix = [[1, 1]]
    print test.maximalSquare(matrix) # = 1

    matrix = [
            [1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0],
            ]
    
    print test.maximalSquare(matrix) # = 4

    matrix = [
            [1,1,1,0,0],
            [1,1,1,1,1],
            [0,0,1,1,1],
            [1,0,1,1,1],
            ]
    print test.maximalSquare(matrix) # = 9

    matrix = [
            [1,1,0,1,1],
            [1,1,1,1,1],
            [0,1,1,1,0],
            [0,1,1,1,0],
            ]
    print test.maximalSquare(matrix) # = 9
