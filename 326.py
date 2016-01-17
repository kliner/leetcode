class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False

test = Solution()
for i in xrange(10):
    print i, test.isPowerOfThree(i)
