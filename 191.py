class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n != 0:
            ret += n & 1
            n >>= 1
        return ret
        
if __name__ == '__main__':
    test = Solution()
    print test.hammingWeight(11)
