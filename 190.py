class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print bin(n)
        r = 0
        for i in range(32):
            r <<= 1
            r |= n & 1
            n >>= 1
        #print bin(r)
        return r

if __name__ == '__main__':
    test = Solution()
    print test.reverseBits(43261596)
