class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        
        T = [int(matrix[0][i]) for i in xrange(n)]
        T.append(0)
        ans = self.findOneRowMax(T)
        for i in xrange(1, m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    T[j] += 1
                else:
                    T[j] = 0
            #print T
            ans = max(ans, self.findOneRowMax(T))
        return ans
    
    def findOneRowMax(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        stack = []
        ans = 0
        for i, x in enumerate(height):
            if not stack or x >= stack[-1][0]:
                stack.append((x, i))
            else:
                while stack and x < stack[-1][0]:
                    t = stack.pop()
                    ans = max(ans, (i - t[1]) * t[0])
                    #print ans, t
                stack.append((x, t[1]))

        return ans


if __name__ == '__main__':
    test = Solution()
    print test.maximalRectangle([
        ['0','0']])
    print test.maximalRectangle([
        ['1','1'],
        ['1','1'],
        ['1','0']])
