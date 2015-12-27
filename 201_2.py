class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        diff = 0
        while m != n:
            m >>= 1
            n >>= 1
            diff += 1

        return m << diff
        
if __name__ == '__main__':
    test = Solution()
    print test.rangeBitwiseAnd(5,7)
    print test.rangeBitwiseAnd(5,8)
    print test.rangeBitwiseAnd(0,1)
    print test.rangeBitwiseAnd(2,3)
