class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n & 1 == 0:
            n >>= 1
        return n == 1

        
if __name__ == '__main__':
    test = Solution()
    print test.isPowerOfTwo(1)
    print test.isPowerOfTwo(2)
    print test.isPowerOfTwo(3)

