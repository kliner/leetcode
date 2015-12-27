class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        if m == n:
            return m
        p = [2**i for i in xrange(32)]
        start = 30
        ans = 0
        while 1:
            for i in xrange(start, -1, -1):
                #print m, n, p[i]
                if m >= p[i]:
                    if n >= p[i+1]:
                        return ans
                    else:
                        m = m-p[i]
                        n = n-p[i]
                        ans += p[i]
                        start = i
                        break
            else:
                return ans

        return ans
        
if __name__ == '__main__':
    test = Solution()
    print test.rangeBitwiseAnd(5,7)
    print test.rangeBitwiseAnd(5,8)
    print test.rangeBitwiseAnd(0,1)
    print test.rangeBitwiseAnd(2,3)
