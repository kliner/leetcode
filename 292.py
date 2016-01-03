class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
        

if __name__ == '__main__':
    test = Solution()
    for i in xrange(1, 10):
        print test.canWinNim(i)
