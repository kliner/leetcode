class Solution(object):

    # bfs, n^0.5 * cnt
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        a = [1]
        while a[-1] < n:
            i+=1
            a.append(i**2)
        marked = [0 for i in xrange(n+1)]
        q = [0]
        cnt = 0
        while 1:
            cnt += 1
            nxt = []
            for num in q:
                for d in a:
                    if num+d == n:
                        return cnt
                    if num+d < n and not marked[num+d]:
                        marked[num+d] = 1
                        nxt.append(num+d)
            q = nxt
 
if __name__ == '__main__':
    test = Solution()
    print test.numSquares(12)
    print test.numSquares(13)
    print test.numSquares(3081)


