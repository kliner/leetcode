class Solution(object):
    def gameOfLife(self, board):
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if board == None:
            return 
        m = len(board)
        if m == 0:
            return 
        n = len(board[0])
        if n == 0:
            return 

        for i in xrange(m):
            for j in xrange(n):
                cnt = 0
                for d in xrange(8):
                    ti = i + dx[d]
                    tj = j + dy[d]
                    if ti >= 0 and ti < m and tj >= 0 and tj < n and board[ti][tj] & 0b01 == 1:
                        cnt += 1
                if cnt in [2, 3] and board[i][j] & 0b01 == 1:
                    board[i][j] = 0b11
                if cnt is 3 and board[i][j] & 0b01 == 0:
                    board[i][j] = 0b10

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = (int) (board[i][j] & 0b10 > 1) 


if __name__ == '__main__':
    test = Solution()
    board = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0],
            ]
    test.gameOfLife(board)
    print board
